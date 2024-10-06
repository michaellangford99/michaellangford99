---
layout: default
title: Power Budget
description: Drone Presentation

eleventyNavigation:
  key: slide_4
  parent: drone_presentation
  
date: 2000-00-06
  
---
<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg align-content-center">


I created a more precise power budget for the particular components and subsystems within the PCB and larger system. I looked up ballpark values for large devices, made estimates, and looked at datasheets. Table 4.1 shows the resulting power budget.

![alt text](IMG_20220927_163218212_HDR.jpg "Initial sketch of power supply cascade")

</div>
<div class="col-lg align-content-center">

<style type="text/css">

</style>

<div class="d-flex justify-content-center">

| Supply             | Device                | Current Typ [mA] | Current Min [mA] | Current Max [mA] |
| ------------------ | --------------------- | ---------------- | ---------------- | ---------------- |
| 4S Battery         | Motor controller(ESC) | 400              | 400              | 400              |
|                    | Motors                | 26000            | 13000            | 38000            |
|                    | 10V Supply            | 439.6            | 184.2            | 567.6            |
| 10V Supply         | 5V Supply             | 424.6            | 169.2            | 552.6            |
|                    | Power LED             | 15               | 15               | 15               |
| 5V Supply          | Radio Receiver        | 3.4              | 3.4              | 3.4              |
|                    | Pi Zero               | 200              | 50               | 250              |
|                    | Camera                | 100              | 50               | 150              |
|                    | Power LED             | 15               | 15               | 15               |
|                    | 3.3V Supply           | 106.2            | 50.8             | 134.2            |
| 3.3V Supply        | STM32 Microcontroller | 80               | 30               | 100              |
|                    | LSM6DSR 6-axis IMU    | 1.2              | 0.8              | 1.2              |
|                    | FT230XQ UART to USB   | 8                | 5                | 8                |
|                    | Power LED             | 15               | 15               | 15               |
|                    | RX/TX LED             | 2                | 0                | 10               |
| Total Current [mA] |                       | 26839.6          | 13584.2          | 38967.6          |
| Total Current [A]  |                       | 26.84            | 13.58            | 38.97            |

</div>
<div class="d-flex justify-content-center">
Table 4.1. Power Budget Results
</div>




</div>
</div>
</div>
</div>