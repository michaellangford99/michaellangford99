import numpy as np
import matplotlib.pyplot as plt

hgt = np.fromfile("N34W118.hgt", np.int16)
hgt = hgt.byteswap()
print(hgt.shape)

height=3601
width=3601
m_per_cell=30

hgt = hgt.reshape((height,width))

plt.imshow(hgt)
plt.show()

normx = hgt[-1:, :]-hgt
normy = hgt[:, -1:]-hgt

normz = np.cross(normx.flatten(), normy.flatten())