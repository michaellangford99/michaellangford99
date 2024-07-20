---
layout: default
title: About Me
description:

eleventyNavigation:
  key: resume
  parent: engineering
  title: resume

templateEngineOverride: njk,md

---

{% macro category(name) %}
<div class="col-lg-2 border-end border-primary">
<div class="d-none d-lg-block text-end"><h6 class="text-primary text-uppercase">{{ name }}</h6></div>
<div class="d-lg-none"><h6 class="text-primary text-uppercase">{{ name }}</h6></div>
</div>
{% endmacro %}

<div class="container">
<div class="row">
<div class="col-2">
<div class="container">
<img src="IMG_9201_cropped3.png" class="figure-img img-fluid rounded-circle">
</div>
</div>
<div class="col-10">
<h1 class="display-1 text-capitalize text-primary">Michael Langford</h1>

<div class="container">
<div class="row">
<div class="col-lg-4 text-muted border-end border-primary">
<a href="mailto:michaellangford99@gmail.com">michaellangford99@gmail.com</a>
</div>
<div class="col-lg-4 text-wrap text-muted border-end border-primary">
7826 S. Windermere Circle, Littleton CO, 80120
</div>
<div class="col-lg-4 text-muted">
(260) 458-7666
</div>
</div>
</div>

</div>
</div>

---

<div class="container">

<div class="row">
{{ category('Summary') }}
<div class="col-10">

Electrical Engineer with a focus in DSP and stochastic signal processing, estimation theory, and applied math; interested in radar, EW, and comms. Familiar with embedded hardware as well, particularly FPGA/ASIC design, embedded software and microcontrollers, and PCB hardware design. 

**DSP Electrical Engineer 2** at **Rincon Research Corporation**, Centennial, CO

**Masters student** in Electrical Engineering with **3.88 GPA** at **Purdue University (May 2025)**

**BS** in Electrical Engineering with **3.97 GPA/Summa cum Laude** from **Purdue University (2022)**

**Active TS/SCI** (IC), **TS**(DoD) **Security Clearances**

</div>
</div>

---

<div class="row">
{{ category('Skills & Abilities') }}
<div class="col-10">

**Work Experience Areas**|**Languages**|**Hardware/Software Tools**
:-----:|:-----:|:-----:
Digital Signal Processing,|Embedded C/C++|MATLAB,
Radar, EW, Comms, RF Analysis,|ARM, Intel, PIC assembly|Multisim,
Algorithms, Modeling/Simulation|VHDL / Verilog / SystemVerilog|Mentor DXDesigner,
PCB,FPGA,ASIC design,|MATLAB, Git, Unix Shell / Bash|Cadence & Kicad PCB Design, Cadence ASIC Design
Controls|C#, Python, HLSL / GPU languages| 

Split into skills that I’m really good at, and those I’m familiar with

Quick learner and hard worker. 
Strong mathematical, hardware, interpersonal, communication and leadership skills.

{% macro field(name) %}
<b>Purdue university student {{ name }} </b>
{% endmacro %}

{{ field('Michael Langford') }}

</div>
</div>

---

<div class="row">
{{ category('Education') }}
<div class="col-10">

<div class="text-uppercase"><b>Purdue university</b> - West Lafayette, IN</div>

- Master’s student in Electrical Engineering, 4.0 GPA, focus in Comms., Network, Signal & Image processing
- Expected graduation: 2024
- (Fall 2022) BS in Electrical Engineering, with 3.97 GPA (with Highest Distinction)
- Dean’s List every semester.
- Coursework: electromagnetics, signal processing,radar, embedded microcontrollers, Verilog ASIC/FPGA design

**Relevant Coursework:**

| ECE438, ECE538 DSP                        | ECE600   Random Variables                                      | ECE678   Radar Engineering              |
|-------------------------------------------|----------------------------------------------------------------|-----------------------------------------|
| ECE637   Image Processing                 | ECE645   Estimation Theory                                     | ECE30412   Advanced Electromagnetics    |
| CT/DT   Math fundamentals                 | Grad. random variables,   distributions, stochastic processes. | Radar fundamentals, detection,   RCS,   |
| FFT, DFT,   filtering, z transforms, etc. | MLE, MMSE, MAP, BLUE, Bayesian,   Kalman filtering             | Antennas, beamforming,                  |
| + Linear   predictive coding              |                                                                | Waveform design,                        |
| + Image   & audio processing              |                                                                | Range doppler processing.               |
| + Radar   & GPS tracking                  |                                                                | Maxwell’s equations, wave   propagation |

**Senior Design:**

**Expand school section**
- Autonomous drone with auto-level and auto-throttle, fully custom flight controller HW & SW via STM32 microcontroller and DSP algorithms in C embedded SW with custom PCB and drone HW assembly.

</div>
</div>

---

<div class="row">
{{ category('Work Experience') }}
<div class="col-10">

<div class="text-uppercase"><b>DSP Electrical Engineer 2</b> - Rincon Research Corporation
<br>
<div class="text-muted">May 2023 – present, Centennial, co</div></div>

-	Radar Waveform Analysis
    -	Wrote large document in Jupyter / Latek detailing performance characteristics and closed-form derivations of various radar waveforms and their CAFs, as well as general radar performance tradeoffs.
    -	Document details closed-form CAF derivation for LFM and WGN, and CAF plots via inline Python and closed form signal definition for LFM, VLFM, NLFM, and WGN.
    -	For WGN waveform this required a stochastic approach and gave a very interesting probability distribution proved out via simulation. For various waveform types derived performance metrics such as range resolution, doppler tolerance, range doppler coupling, etc.
    -	Worked towards derivation of MLE estimator for delay and doppler, covariance of CAF between transmitted and noise corrupted signal. Wrote additional Python programs to simulate waveform performance and verify calculations, compute hessian of CAFs, and noise corrupted cross-ambiguity function computation.

- TODO: insert info that you need to expand upon and vet.

-	OpenGL 3D Tracking Visualizer
    -	Built 3D OpenGL program from scratch to visualize live radar tracking data, designed with an extendible framework to allow easy usage for other projects.
    -	Implemented complex graphical elements via GLSL shaders to draw translucent 3D cones, ellipsoids, cubes, etc. to display relevant scene information such as target estimate uncertainty, radar beamwidth and orientation, and tracks of known or estimated targets.
    -	All elements can be animated, and all scene properties easily edited via programmatically generated GUI. Program is being interfaced with a live database from which it will pull current radar and tracking data and display in real time.

<!--</div>
</div>

---

<div class="row">
<div class="col-2 border-end border-primary"><h6 class="text-primary text-uppercase text-end">Internships</h6></div>
<div class="col-10">-->

<div class="text-uppercase"><b>RF / MSIC Engineering Intern</b> - BAE Systems [FASTLabs MSIC Team]
<br>
<div class="text-muted">May 2022 - August 2023, Merrimack, NH</div></div>

-	MSIC design group creates RF ASICS for BAE FASTLabs, DARPA, DoD, etc. Used for radar / EW / Comms.
-	MATRICs LO PLL digital calibration module fault investigation / modeling
    -	Investigated issues with in-production PLL calibration system. On-chip LO generated using 4 LC VCOs covering 10-22GHz range, using digital control and calibration module.
    -	Developed testbenches and simulation environment for autocalibration module in SystemVerilog.
    -	Testbenches emulated the SPI interface to the module and imitated real world use cases.
    -	Created physically accurate time domain Verilog model for analog PLL to interface to testbenches.
    -	Tested operation of algorithm on hardware, using spectrum analyzer and SPI bus interface to chip. 
-	Cadence IC layout and schematic training and experience, learning MSIC process/design flow. Helped create example Verilog, synthesis, place & route scripts, etc. to demonstrate digital design flow.
-	RF amplifier analysis via Cadence simulations and Matlab + hand calculations
-	Hand calculation of transfer functions, implemented in Matlab and compared to simulations.
-	Analyzed pole movement over parameter sweeps to determine stability and dominant parasitics.
-	RF ASIC Ka band transceiver conversion gain measurements and debugging / de-embedding
    -	Measured conversion gain across power to identify nonlinearity in transmit path. Custom VNA setup to account for trace+cable loss, and processed results from VNA across 5 boards to remove output loss. 

<div class="text-uppercase"><b>Undergraduate Research</b> - Superresolution Imaging, Webb Group, Purdue University
<br>
<div class="text-muted">Jan 2022 - May 2022, West Lafayette, IN</div></div>

-	Undergrad Research for credit with Webb Group, supporting superresolution imaging using photon counting.
-	Characterized new photon counting equipment using SPAD detector and pulsed laser. Developed algorithms in MATLAB and Python to analyze results, and detect and remove vibration, optical multipath, modal dispersion.
-	Literature review including review of phase recovery algorithm via triple correlation in HBT interferometer.

<div class="text-uppercase"><b>Electrical Engineering Intern</b> - Raytheon Missiles & Defense
<br>
<div class="text-muted">May 2021 - April 2022, Tucson, AZ</div></div>

- Continued to support active projects during entirety of school year while remote, ~15+ hr/wk. 
-	Air-to-air, active radar guided anti-drone missile IRAD team
    -	Developed Missile to Engineer test interface between missile guidance CCA stack and engineers for integration. App is a data exchange system split into a client server model to allow either C# GUI or Python scripts as client and C++ server for communications to the missile.
    - Led 2 engineers to complete project as the lead software designer while working remote during school.
    - System controls power supplies, temp monitoring and safe startup/shutdown; intercepts and displays all intra-missile comms, controls CCAs via a proprietary network protocol.
    - System fills an important gap in testing capability from old by-hand methods allowing software team to immediately verify their software design objectives and write simple Python scripts to interface to missile.
    - Provided a critical component of the integration system for the project.

<div class="text-uppercase"><b>Teacher's Assistant</b> - ECE Dept, Purdue University</div>

- Teacher’s Assistant – ECE438 Digital Signal Processing - Fall 2022
- Teacher’s Assistant – ECE270 Digital Logic Design - Spring 2021

<div class="text-uppercase"><b>Electrical Engineering Intern</b> - UTEC (United Technologies Electronic Controls)
<br>
<div class="text-muted">June 2020 - May 2021, Fort Wayne, IN</div></div>

-	OTIS Elevator counterweight motion DSP safety system 
    -	System senses motion in elevator counterweight using accelerometer, sounds alarm whenever device is in motion. Purpose is preventing crush injuries at sites where elevator shaft is not yet enclosed.
    -	Created initial prototype with available processors and MEMS accelerometer for testing.
    -	Developed embedded C/C++ software and signal processing algorithms to integrate and filter acceleration data to determine estimate of elevator velocity without drift. Testing at sites demonstrates that software correctly distinguishes constant acceleration from a stopped counterweight.
    -	Created simulation environment in MATLAB to test filters/algorithm on recorded acceleration data
    -	Primary designer of schematic for production device using MEMS device and faster PIC32. 
    -	Patent pending, was awarded by company for role in device creation.

<div class="text-uppercase"><b>Electrical Engineering Intern</b> - UTEC (United Technologies Electronic Controls)
<br>
<div class="text-muted">June 2019 - August 2019, Huntington, IN</div></div>

-	Rehired after freshmen year of college, focusing on continued hardware engineering and circuit / PCB design

<div class="text-uppercase"><b>Electrical Engineering Intern</b> - UTEC (United Technologies Electronic Controls)
<br>
<div class="text-muted">February 2018 - August 2018, Huntington, IN</div></div>

-	Hired upon early graduation from high school. Focused on Embedded SW with C & PIC32 micros.

<div class="text-uppercase"><b>Personal Projects</b></div>

-	Autonomous Quadcopter:  Designed and built mechanical and electrical parts and wrote all software.
Embedded C/C++ SW processes sensors and radio control commands via DSP and PID control loops, and outputs to motors via PWM. Flies and self-levels.
-	Intel x86 Kernel: Wrote a basic kernel in C and x86 assembly with working process management, memory allocation and paging, memory protection, graphics, written from scratch.
- ADD OPENGL PROJECTS

</div>
</div>

---

</div>
