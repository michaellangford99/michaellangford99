---
layout: default
title: PCB design
description:

eleventyNavigation:
  key: slide_pcb
  parent: drone_presentation
  
date: 2000-00-11

---



<div class="carousel-item " style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">

<div class="row">
<div class="col-lg-6 ml-auto mr-auto align-content-center">

![alt text](../wk6/image015.png "Initial footprint positioning") 

![alt text](../wk6/image017.png "Rendered view")

</div>

<div class="col-lg-1 ml-auto mr-auto align-content-center"></div>
<div class="col-lg-4 ml-auto mr-auto align-content-center">

![alt text](image-3.png "Working on the FTDI section")

</div>

<div class="col-lg-1 ml-auto mr-auto align-content-center"></div>
</div>
</div>
</div>

<!--
INSERT PCB design section
-->
<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>
<div class="container align-content-center" style="height: 100%">

![alt text](pcb.png "Kicad PCB view")

</div>
</div>

<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>
<div class="container align-content-center" style="height: 100%">

![alt text](ECE477_PCB.png "3D render with part models")

</div>
</div>

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
