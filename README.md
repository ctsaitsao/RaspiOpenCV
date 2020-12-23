# Raspberry Pi Performance Testing using Computer Vision
Project for ME 399: Independent Study, Summer 2019. Advisor: Nick Marchuk.

## Overview
This project aimed to test the performance of the two latest Raspberry Pi models at the time: the Pi 3 Model B+ and the Pi 4 Model B. This consisted of running a program on both Pi models and comparing the way the program executed. For this project, the program of choice was a face detection algorithm that also commanded a robot arm's movement to follow a person's face in two directions. Performance testing involved observing how the program ran, outputting time data, and plotting the control system’s performance.

## Hardware
A SainSmart 6-Axis Desktop Robotic Arm was used alongside a Polulu Micro Maestro 6-channel USB Servo Controller. The controller has 6 connections for servos and can be powered by USB or a 5-16V pin input. The servos themselves were powered by a laptop charger (their cables were soldered to the charger).

![](images/arm.png)

![](images/controller.png)

For vision, a Raspberry Pi camera was attached to the end effector of the robot arm.

![](images/camera.jpg)

## Software
### Dependencies
- The OpenCV Python library was used for face detection. Its `cv2.CascadeClassifier` class uses a Haar Cascade to detect faces.
- [This repo](https://github.com/FRC4564/Maestro) contains a file called `maestro.py` which utilizes Python’s serial module (pySerial) to communicate with the Maestro controller.

### Workflow


### Setup and Usage
1. After installing OpenCV and pySerial, download the `maestro.py` module:
   ```
   wget https://raw.githubusercontent.com/FRC4564/maestro/master/maestro.py
   ```
2. All code resides in `code/main.py`. Simply run:
   ```
   python main.py
   ```

Using a PI control loop, I programmed the arm to follow my face in two directions (x and y). The “performance testing” thus became observing how the program ran, outputting time data, and plotting the control system’s performance.


