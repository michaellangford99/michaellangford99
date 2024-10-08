---
layout: default
title: IMU design and integration
description:

eleventyNavigation:
  key: slide_imu
  parent: drone_presentation
  
date: 2000-00-12

---

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>
<div class="container align-content-center" style="height: 100%">

**IMU chips**
- I selected the LSM6SO for its cheapness and availability (this was during the chip shortage)
- The MPU9250 is a tried and true part that I've worked with in the past and so was used to lower risk.
- Both are SPI based MEMS IMU devices, interfaced via writing register table for configuration and polling for IMU data

<div class="row">
<div class="col-lg-5 align-content-center">

![alt text](image-1.png "MPU9250 block diagram")

</div>
<div class="col-lg-7 align-content-center">

![alt text](image-2.png "LSM6DSO block diagram")

</div>
</div>
</div>
</div>

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>
<div class="container align-content-center" style="height: 100%">

**Initial results**

The first objective after verifying my SPI bus driver was to begin streaming data off the devices, and tuning their configurations. Starting out, the data was too slow, and had the wrong bit format, but after fixing the bit shifting etc., and setting a higher data rate, it was clear all 6 axes were being properly read.

![Alt text](../wk10/image.png "Fig. 10.1. 6 axes being read, accelerometer X,Y,Z, and gyro X, Y, Z.")

</div>
</div>

<!-- 
add in here some info about the SPI driver and initial dev?
-->

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>
<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-6 align-content-center">

**IMU Calibration**

Next, all channels of the IMU must be calibrated so that the average value returned by the gyro for angular rate would be zero. Otherwise the integration of the angular rate to get heading would result in immediate drift and a useless measurement. Therefore, the system sums up for each axis a few thousand readings at reasonable time intervals, then divides that sum by the umber of samples to get the average reading. That is then subtracted from all future readings to get a zero mean angular rate reading.

![Alt text](../wk10/image-5.png "Fig. 10.6. Integrated gyro heading data (before scaling applied)")

</div>
<div class="col-lg-6 align-content-center">

```c
for (int i = 0; i < CAL_LENGTH; i++)
	{
		//set precise sampling interval
		wait(1.0f/(6.67f*1000.0f));

		read_axes();
		gyro_cal_x += gyro_raw_x;
		gyro_cal_y += gyro_raw_y;
		gyro_cal_z += gyro_raw_z;

		accel_cal_x += accel_raw_x;
		accel_cal_y += accel_raw_y;
		accel_cal_z += accel_raw_z - A_RAW_1G; //Z axis experiences gravity, this cals it to 1G
	}

	gyro_cal_x = gyro_cal_x / CAL_LENGTH;
	gyro_cal_y = gyro_cal_y / CAL_LENGTH;
	gyro_cal_z = gyro_cal_z / CAL_LENGTH;

	accel_cal_x = accel_cal_x / CAL_LENGTH;
	accel_cal_y = accel_cal_y / CAL_LENGTH;
	accel_cal_z = accel_cal_z / CAL_LENGTH;
```

*Fig. 10.5. Calibration code*

</div>
</div>
</div>
</div>

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>
<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-4 align-content-center">

Once this was clearly working, I created a working timing driver to measure sub-millisecond time deltas as well as those with sub-millisecond fidelity but multi-millisecond span.

To do this, I combined the Systick timer’s countdown register, and a ‘tick’ variable incremented on every systick interrupt. I calculated the Systick roll-over value based on the clock frequency such that the interrupt occurs once every millisecond, giving a simple 1KHz timer.

</div>
<div class="col-lg-8 align-content-center">

```c
#define AHB_CLOCK 		SystemCoreClock		//48 MHz
#define AHB_CLOCK_DIV_8 (AHB_CLOCK/8)	//6 MHz
#define SYSTICK_INT_FREQ 1000			//1KHz desired interrupt frequency
#define SYSTICK_LOAD	((AHB_CLOCK_DIV_8/SYSTICK_INT_FREQ)-1)

void init_SYSTICK()
{
	SysTick->LOAD = SYSTICK_LOAD;
	SysTick->VAL = 0;

	SysTick->CTRL |= (1<<0);
	SysTick->CTRL |= (SysTick_CTRL_TICKINT_Msk | SysTick_CTRL_ENABLE_Msk/* | SysTick_CTRL_CLKSOURCE_Msk*/);

	printf("SYSTICK:\n");
	printf("\tSYSTICK_LOAD:		%d\n", SYSTICK_LOAD);
	printf("\tAHB_CLOCK:		%d\n", AHB_CLOCK);
	printf("\tAHB_CLOCK_DIV_8:	%d\n", AHB_CLOCK_DIV_8);
}
```

</div>
</div>
</div>
</div>

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>
<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-4 align-content-center">

To calculate inter-interrupt timing, I use the value of the systick down-counting register to determine how many decrements remain before rollover. When compared to the clock frequency (how many decrements per second), a floating point time in units of seconds can be calculated. I still need to determine however if fixed point math would be better suited to this though. The STM32F4 has an FPU to accelerate these calculations, although 32 bit fixed point may be better.

Once this was created, I could calculate the precise timestep between readings of the gyro data. This is crucial for accurate integration of the gyro angular rate data. Although much remains to be configured in terms of low pass filters, aliasing prevention, etc. I was able to obtain unit-correct heading data.

</div>
<div class="col-lg-8 align-content-center">

```c
uint32_t ticks = 0;
void SysTick_Handler(void) {
	ticks++;
    ...
}

...

float ftime() {
	return ((float)ticks/(float)SYSTICK_INT_FREQ) + (float)(SYSTICK_LOAD-SysTick->VAL)/(float)AHB_CLOCK_DIV_8;
}
```

*Fig. 10.3. Code to calculated floating point timestamp in seconds.*

```c
read_axes();

last_time = current_time;
current_time = ftime();

gyro_rate_x = (gyro_raw_x - gyro_cal_x) * G_GAIN_500DPS;
...

gyro_angle_x += gyro_rate_x * (current_time - last_time);
...
```

*Fig. 10.4. Code sample including LSB scaling and time delta.*

</div>
</div>
</div>
</div>