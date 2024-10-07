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

![alt text](ECE477_PCB.svg "TODO: slice this thing up into pieces")

</div>
</div>

<!--
INSERT sections of schematic design
-->

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

<!--
INSERT PCB design section
-->

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-7 align-content-center">

I also added the PI Zero connector that I had put off for last, selecting a part of the Pi header to interface to that contains the UART, +5V, and ground. This is pins 1 through 10 at the far edge of the PI PCB. This ended up being a relatively convenient spot after I moved a couple things out of its way.

![Alt text](../wk7/image-2.png "Pi Zero pinout")

</div>
<div class="col-lg-5 align-content-center">

![Alt text](../wk7/image-3.png "Pi Zero dimensions")

![Alt text](../wk7/image-4.png "PCB drill and borders plot")

</div>
</div>
</div>
</div>

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg-6 align-content-center">

Now that the part was in the ~mostly correct spot, I had to ensure that the connector would line up perfectly by looking up the exact dimensions of the board, and by verifying the setup by printing a to-scale version of the board and checking it against the Pi Zero I own.

Using these measurements, I worked to place it in what I believed was the best position. Then I printed off the to-scale version and compared. I noticed that while all the corner holes were properly aligned, the connector was about a millimeter too far to the right. I then readjusted and printed again. Much better! A visual check shows the pins at the exact right spot.

![Alt text](../wk7/image-6.png "PCB size comparison")

</div>
<div class="col-lg-6 align-content-center">

![Alt text](../wk7/image-5.png "Pi zero with footprint printout")

</div>
</div>
</div>
</div>
