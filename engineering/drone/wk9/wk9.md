---
layout: default
title: ECE477 Drone
description:

eleventyNavigation:
  key: wk9
  parent: drone
  title: wk_9

---

# Week 9

**PCB Design**

This week was mostly spent finishing the schematic and PCB layout for the flight controller. I took the input and corrections gathered from the midterm design review and implemented that guidance on the board design.

The critical points noted during the design review were:
•	Extend pads on QFN for IMUs and FTDI
•	Fix voltage divider inversion
•	Add capacitor on VSense
•	Remove ground plane around and beneath oscillator
•	Change footprint of voltage regulator to the actual footprint, rather than a footprint of equal size and pads with improper silkscreen and boundary.

![Alt text](image.png "Fig. 8.1. Resizing pads on LSM6DS3 to allow for easier hand soldering.")

![Alt text](image-1.png "Fig. 8.2. Fixed voltage divider setup for VSense.")

![Alt text](image-2.png "Fig. 8.3. Added keepouts below and surrounding oscillator.")

The fix for the voltage regulator was significantly more involved. I first had to find a 3D model for the part itself, which luckily Pololu provides as a .STEP file, a common Autodesk part file. I then struggled with multiple export utilities, trying to find one that would export to .WRL (KiCAD’s supported 3D model filetype), but retain it’s material / color information.

After a few tries, I then imported the model file and set its position, scale and the boundary for the footprint.

![Alt text](image-3.png "Fig. 8.4. Correct 3D model of footprint.")

![Alt text](image-4.png "Fig. 8.5. Regulator correctly imported into rest of PCB 3D model.")