# Raspberry Pi Performance Testing using Computer Vision
Project for ME 399: Independent Study, Summer 2019. Advisor: Nick Marchuk.

## Overview
This project aimed to test the performance of the two latest Raspberry Pi models at the time: the Pi 3 Model B+ and the Pi 4 Model B. This consisted of running a program on both Pi models and comparing the way the program executed. For this project, the program of choice was a face detection algorithm that also commanded a robot arm's movement to follow a person's face in two directions using PI control. Performance testing involved observing how the program ran, outputting time data, and plotting the control system’s performance.

## Hardware
A SainSmart 6-Axis Desktop Robotic Arm was used alongside a Polulu Micro Maestro 6-channel USB Servo Controller. The controller has 6 connections for servos and can be powered by USB or a 5-16V pin input. The servos themselves were powered by a laptop charger (their cables were soldered to the charger).

![](media/arm.png)

![](media/controller.png)

For vision, a Raspberry Pi camera was attached to the end effector of the robot arm.

![](media/camera.jpg)

## Software
### Dependencies
- The OpenCV Python library was used for face detection. Its `cv2.CascadeClassifier` class uses a Haar Cascade to detect faces.
- [This repo](https://github.com/FRC4564/Maestro) contains a file called `maestro.py` which utilizes Python’s serial module (pySerial) to communicate with the Maestro controller.

### Workflow
In a nutshell, the code detects faces and uses the x,y distance of the faces to the midpoint of the video feed to send a signal to two of the robot arm's servos. The servos try to correct the position discrepancy by moving the robot until the face lies in the midpoint of the image.

### Pseudocode
1. Initialize all servos to a home position.
2. Initialize controller variables.
3. While true:
   1. Detect faces and draw face rectangles using `detectMultiScale` function.
   2. For each face:
      1. Initialize reference value (midpoint of window) and sensor value (midpoint of face rectangle) for both x and y directions.
      2. Acquire position error (distance between midpoint of window and midpoint of rectangle) for both x and y directions.
      3. Feed position targets (which depend on position error) to the servos that control x,y movement.
4. If break signal is detected, plot error results.

### Setup and Usage
1. After installing OpenCV and pySerial, download the `maestro.py` module:
   ```
   wget https://raw.githubusercontent.com/FRC4564/maestro/master/maestro.py
   ```
2. All code resides in `code/main.py`. Simply run:
   ```
   python main.py
   ```
   
## Demo
