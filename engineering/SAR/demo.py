import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

c = 3e8
fs = 100e6

fc = 2.4e9
scene_center_range=200
scene_width_range=500
ac_start_pos = np.array([0,10.0,-1.0])
ac_pos = ac_start_pos
ac_vel = np.array([0,0,1.0])

flight_distance = 2.0

#targets_pos = np.array([[-scene_center_range-200, 0.0, 1.0],
#                        [-scene_center_range-100, 0.0, 4.0]])

#targets_pos = np.zeros((200,3))

#for i in range(100):
#    targets_pos[i,:] = np.array([-scene_center_range-3*i, 0, i/100.0])
#for i in range(100):
#    targets_pos[100+i,:] = np.array([-scene_center_range+3*i-300, 0, i/100.0])

#now try using a slice of terrain
hgt = np.fromfile("N34W118.hgt", np.int16)
hgt = hgt.byteswap()
print(hgt.shape)

height=3601
width=3601
m_per_cell=30

hgt = hgt.reshape((height,width))

decimation = 4

hgt = hgt[::decimation, ::decimation]

sl_w = 50
sl_h = 50
sl_y = int(2150/decimation)
sl_x = int(300/decimation)
hgt = hgt[sl_y:sl_y+sl_h,sl_x:sl_x+sl_w]

hgt_deriv = hgt - np.roll(np.roll(hgt, shift=1, axis=0), shift=1, axis=1)

plt.imshow(hgt)
plt.show()

plt.imshow(hgt_deriv)
plt.show()

targets_pos = np.zeros((sl_w*sl_h,3))
for i in range(sl_h):
    for j in range(sl_w):
        targets_pos[i*sl_w+j] = np.array([-scene_center_range-j - 10, (hgt[i,j]-1300)/10, i/50.0])
        print(f"{targets_pos[i*sl_w+j]=}")

plt.scatter(targets_pos[:,0], targets_pos[:,2])
plt.show()

max_doppler_freq = fc*np.sqrt(np.sum(ac_vel**2))/c
print(f"{max_doppler_freq=}")

pri = 3000e-6#2/max_doppler_freq
prf=1/pri
df  = 0.1
bw  = 100e6

print(f"{pri=}")
print(f"{prf=}")

k = bw/(df*pri)
pulse_samples = int(df*pri*fs)
t = np.arange(0, pulse_samples)/fs
lfm = np.exp(1j*2*np.pi*0.5*k*t**2+1j*2*np.pi*(-bw/2)*t)

#plt.plot(t, lfm.real)
#plt.plot(t, lfm.imag)
#plt.savefig('lfm')

#for now, model returns as a spike at the delay and phase proper to their location
#how many range bins though? idk how much to discretize

range_res = c*(1.0/bw) #/2?
print(f"{range_res=}")

total_pulses = int((flight_distance/np.linalg.norm(ac_vel, 2))/pri)
print(f"{total_pulses=}")

max_unanmbig_range = c*pri/2
print(f"{max_unanmbig_range=}")

max_unambig_doppler = 1/(2*pri)
print(f"{max_unambig_doppler=}")

range_cells = int(max_unanmbig_range/range_res)
print(f"{range_cells=}")

range_cells_scene = int(scene_width_range/range_res)

data = np.zeros((total_pulses, range_cells_scene), np.complex64)

target_prior_phase = np.zeros(targets_pos.shape[0])

for p in range(total_pulses):
    #compute range to target
    #compute doppler to target
    #generate response position and phase in fast time

    target_ranges = np.linalg.norm(targets_pos - ac_pos, 2, axis=1)
    target_range_rates = -np.dot(ac_vel, (targets_pos-ac_pos).T)
    target_dopplers = fc*target_range_rates/c

    #print(f"{target_dopplers=}")

    #print(f"{target_ranges=}")

    range_phase = 2*np.pi*target_ranges%(c/fc)

    phase_progression = 2*np.pi*target_dopplers/prf

    target_phase = target_prior_phase+phase_progression

    target_time_delays = target_ranges/c
    target_range_bins = target_ranges/range_res

    #print(f"{target_range_bins.astype(np.int64)-int(scene_center_range/range_res)=}")

    #print(f"{target_range_bins=}")

    for i in range(target_range_bins.size):
        pwr = np.abs(hgt_deriv[int(i/sl_w), i%sl_w])**2
        data[p,int(target_range_bins[i])-int(scene_center_range/range_res)] += np.exp(1j*(target_phase[i]+range_phase[i]))#*pwr

    ac_pos += ac_vel*pri
    target_prior_phase = target_phase

    print(f"{p=}")

#trim to scene

range_offset = int((scene_center_range-100)/range_res)
range_width = int(2*sl_w*30/range_res)

#data = data[:,range_offset:(range_offset+range_width)]

plt.imshow(np.angle(data), aspect=data.shape[1]/data.shape[0])
plt.show()
#plt.savefig('data_phase', dpi=600)


plt.imshow(np.abs(data)**2, aspect=data.shape[1]/data.shape[0])
plt.show()
#plt.savefig('data_mag', dpi=600)

#mf_result = np.zeros((total_pulses*2+1, range_cells), np.complex64)

#each range bin gonna need its own matched filter i guess
for i in range(data.shape[1]):
    #generate the matched filter
    r=range_offset+i
    #lets just generate the phase history for a target at [0,r] and matched filter for that
    #just ignore the range migration

    mf_pulses = total_pulses
    ac_s_pos = -ac_vel*pri*mf_pulses/2

    positions = ac_s_pos+np.outer(np.arange(mf_pulses), pri*ac_vel)
    range_bin_center_pos = np.array([-r, 0, 0])
    target_range_rates = -np.dot(ac_vel, (range_bin_center_pos-positions).T)
    target_dopplers = fc*target_range_rates/c
    phase_progression = 2*np.pi*target_dopplers/prf
    phase_arg = np.cumsum(phase_progression)

    #ranges = np.linalg.norm(range_bin_center_pos-positions, 2, axis=1)
    #range_phase = 2*np.pi*target_ranges%(c/fc)

    mf = np.exp(1j*(phase_arg))

    #plt.plot(mf.real)
    #plt.plot(mf.imag)
    #plt.show()
    
    #matched filter
    data[:,i] = np.fft.fftshift(np.fft.ifft(np.fft.fft(data[:,i]) * np.fft.fft(np.conj(np.flipud(mf)))))

    #print(f"{r=}")

plt.imshow(np.abs(data)**2, aspect=data.shape[1]/data.shape[0])
plt.show()

clip = data
clip[np.abs(data) < 0.01*np.max(np.abs(data))] = 0

plt.imshow(np.angle(clip), aspect=data.shape[1]/data.shape[0])
plt.show()

plt.imshow(np.real(clip), aspect=data.shape[1]/data.shape[0])
plt.show()