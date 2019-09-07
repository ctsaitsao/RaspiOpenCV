import cv2
import numpy as np
import maestro
import time
import matplotlib.pyplot as plt

### Defining function that returns moving averages of a list:
#
# def movingaverage(values, window):                              # simple moving average function
#      weights = np.repeat(1.0, window)/window
#      smas = np.convolve(values, weights)
#      return smas

## Setting servo starting positions:

servo = maestro.Controller('/dev/ttyAMA0')

servo.setAccel(5,4)                                             # set servo 5 acceleration to 4
servo.setTarget(5,1000)                                         # set servo to move to far left position
servo.setSpeed(5,10)                                            # set speed of servo 5

servo.setAccel(4,4)                                             # set servo 4 acceleration to 4
servo.setTarget(4,6400)                                         # set servo to move to center-right position
servo.setSpeed(4,10)                                            # set speed of servo 4

servo.setAccel(1,4)                                             # set servo 1 acceleration to 4
servo.setTarget(1,6000)                                         # set servo to move to far right position      ## Y AXIS
servo.setSpeed(1,10)                                            # set speed of servo 1

servo.setAccel(3,4)                                             # set servo 2 acceleration to 4
servo.setTarget(3,6000)                                         # set servo to move to center position
servo.setSpeed(3,10)                                            # set speed of servo 2

servo.setAccel(2,10)                                            # set servo 2 acceleration to 10
servo.setTarget(2,6000)                                         # set servo to move to center position         ## X AXIS
servo.setSpeed(2,10)                                            # set speed of servo 2

## Importing Haar Cascade:

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

## Declaring error variables:

edotx= 0
eprevx = 0
eintx = 0
edoty= 0
eprevy = 0
einty = 0

## Setting gain parameters:

Kpx = 1.8
Kix = .3
Kdx = 0
Kpy = 15
Kiy = 1
Kdy = 0

# i = 0                                                           # counter

## Declaring list variables:

# ex_list = []
# ey_list = []
sx_list = []
sy_list = []

time.sleep(1)                                                   # one second so robot has time to move to start position

while True:
    start = time.time()                                         # to measure time of one iteration
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,+ 5)        # finds faces; depending of size of image and likelihood of finding objects you would change these numbers
    
    for (x,y,w,h) in faces:                                     # draws rectangle on detected faces, which are ndlistays of [[x y z h]]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)     # starting pt x,y; ending pt x+w, y+h; blue; line width 2
        
        rx = 320                                                # r = reference value = midpoint of window
        sx = x + w/2                                            # s = "sensor value" = midpoint of rectangle
        ex = rx - sx                                            # e = error = difference b/w midpoint of window and midpoint of rectangle
#         ex_list.append(ex)
        sx_list.append(sx)
        
        ry = 200                                                # reference value of w, aka the reference distance we want the robot to be from the person at any given time
        sy = w                                                  # "sensor value" is just the variable w
        ey = ry - sy
#         ey_list.append(ey)
        sy_list.append(sy)
        
#         ex_list_avg = movingaverage(ex_list, 3)
#         ey_list_avg = movingaverage(ey_list, 3)
        
    
        eintx = eintx + ex
#         edotx = ex_list_avg[i]
        edotx = ex - eprevx
        
        einty = einty + ey
#         edoty = ey_list_avg[i]
        edoty = ey - eprevy
                    
        ux = Kpx*ex + Kix*eintx + Kdx*edotx
        uy = Kpy*ey + Kiy*einty + Kdy*edoty
        
        servo.setTarget(2, 6000 + int(ux))
        servo.setTarget(1, 6000 - int(uy))                      # minus because we want servo value to decrease as w increases and vice versa 
            
        eprevx = eprevx + ex
        eprevy = eprevy + ey   
        
#         i += 1
    
    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):                       # press 'q' to quit
        break
    
    stop = time.time()
    print(stop - start)                                         # time difference in seconds

## Creating lists that contain the reference values (so that the reference values can be graphed):  

rx_list = [320]*len(sx_list)
ry_list = [200]*len(sy_list)    

## Graphing:

fig, axs = plt.subplots(2)
fig.suptitle('PID Control Plots: Reference Values vs. "Sensor" Values')
axs[0].plot(sx_list, label = 'sx')
axs[0].plot(rx_list, label = 'rx')
axs[0].legend()

axs[1].plot(sy_list, label = 'sy')
axs[1].plot(ry_list, label = 'ry')
axs[1].legend()

plt.xlabel('Iteration')
plt.show()
    
cap.release()
cv2.destroyAllWindows()
servo.close()