---
layout: default
title: Schematic
description:

eleventyNavigation:
  key: slide_schematic
  parent: drone_presentation
  
date: 2000-00-10

---

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%; width: 120%">

![alt text](ECE477_PCB.svg "Final schematic (IMU is on its own page)")

</div>
</div>


<!--
INSERT sections of schematic design
-->

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-5 align-content-center">

**Power and status**
- Power is provided through ESC connector `J3`
- 10V power is regulated down to 5V and then 3.3V
- External power connector option available
- Status LEDs for each supply

</div>
<div class="col-lg-7 align-content-center">

![alt text](<svg/ECE477_PCB-cropped.svg> "Power and status section")

</div>
</div>
</div>
</div>


<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-4 align-content-center">

**USB UART**
- USB micro-B allowed easy serial connection to the flightcontroller
- Small and configurable FT230XQ in QFP package supports power over USB and indicator LEDs

</div>
<div class="col-lg-8 align-content-center">

![alt text](<svg/ECE477_PCB-cropped (1).svg> "FTDI UART")

</div>
</div>
</div>
</div>




<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-4 align-content-center">

**STM32 and peripherals**
- STM32F446 220MHz CPU
- Radio, Pi, and auxiliary UARTs
- voltage sense
- PWM outputs
- reset, external crystal, cap banks

</div>
<div class="col-lg-8 align-content-center">

![alt text](<svg/ECE477_PCB-cropped (2).svg> "STM32")

</div>
</div>
</div>
</div>

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-4 align-content-center">

**LiDAR and backup motor drivers**
- I2C bus connections for LiDAR ToF sensors
- backup brushed motor drivers using simple FET drivers
  in case we had to abandon the brushless motors

</div>
<div class="col-lg-8 align-content-center">

![alt text](<svg/ECE477_PCB-cropped (4).svg> "LiDAR and brushed motors")

</div>
</div>
</div>
</div>

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-7 align-content-center">

**PCB Design**

As things move around, the optimal location to have the signal pins originate off the microcontroller can change. So, in addition to selecting optimal final locations for the components, I frequently checked the datasheet, and a handy ST tool to check which UARTs, SPI busses, etc. could be enabled on which IO pins. Using this, I could validate that my pin configuration was workable with my physical layout, and then implement that on my schematic.

Implementing the IMU was mildly interesting, as I want the capability to use either the MPU9250, the LSM6DS3, or both. So in addition to adding the recommended parts, caps, etc., I added a network of 0 ohm resistor switches to enable the desired configuration as needed.

![Alt text](../wk7/image-1.png "Dual IMU configuration")

</div>
<div class="col-lg-5 align-content-center">

![Alt text](../wk7/image.png "STM32F446 pin mappings")

</div>
</div>
</div>
</div>
