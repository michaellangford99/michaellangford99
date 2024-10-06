---
layout: default
title: Initial part selection
description: Drone Presentation

eleventyNavigation:
  key: slide_1
  parent: drone_presentation
  
date: 2000-00-02

---
<div class="carousel-item" style="height: 100%">
<h1 class="text-center mt-3">{{ title }}</h1>

<div class="container align-content-center" style="height: 100%">
<div class="row">
<div class="col-lg align-content-center">

**Parts selection & Weight / Current / Thrust calculations**

In order to determine the proper parts to order for the drone itself, i.e. the frame, motors, battery, propellers, and motors controller, I had to do extensive research.

This week I worked on, and have nearly completed, determining the correct parts. I started with the physical frame, choosing the size that would allow the electronics necessary for completing the project.

This necessitated a 5” size drone frame (5” propellers). 

Next, I created a complex spreadsheet to calculate the necessary battery capacity for a minimum flight time, given inputs concerning the motor thrust, current, and drone parts’ weights.

The spreadsheet first calculates the total weight of the drone, taking into account each part. Prospective parts can be entered so as to see if, for example, a motor controller provides enough current but is too heavy.

With the full weight calculated, the thrust is the next necessary calculation. Using propeller-motor pair data available online for ubiquitous motor-propeller combinations, along with seller data, the current at 75% throttle and the thrust at that throttle could be entered.

From the thrust-current measurement, a crude linearization gives the amps of current per gram of thrust - amps per unit thrust 

$$\left[\frac{A}{g}\right]=\frac{current @ 75pct throttle [A]}{ thrust @ 75pct throttle [g] }$$.

</div>
<div class="col-lg align-content-center">

<div class="d-flex justify-content-center">


|Minimum Flight Time|	120|	seconds|
|-|-|-|
|frame weight|	100|	grams|
|motor weight|	126.4|	grams|
|propellers|	4|	grams|
|4in1 ESC weight|	21|	grams|
|radio reciever|	2|	grams|
|single-board computer|	10|	grams|
|flight controller|	20|	 |
|camera|	4|	 |
|Typical 4S 1200mAh battery|	100|	grams|
|additional wiring|	20|	grams|
|total weight|	407.4|	grams|
| |	 |	 |
|thrust from chosen 2306 brushless|	1526|	grams|
|amps at above thrust|	51.3|	A|
|amp/g thrust|	0.0336173|	A/grams|
| |	 |	 |
|total thrust necessary|	1222.2|	grams (3x drone weight)|
|thrust per motor|	305.55|	grams|
|current at given thrust|	3.423922018|	A|
|processor and nav current|	3|	A|
|total current|	16.69568807|	(4x motor current, +FC current)|
| |	 |	 |
|hours of flight time|	0.033333333|	h|
| |	 |	 |
|mAh necessary|	556.5229358|	mAh|

</div>

</div>
</div>
</div>


</div>