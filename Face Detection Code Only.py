import cv2
import numpy as np

# https://github.com/opencv/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)   # finds faces; depending of size of image and likelihood of finding objects you would change these numbers
    
    for (x,y,w,h) in faces:      # draws rectangle on detected faces
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)    # starting pt x,y; ending pt x+w, y+h; blue; line width 2
    
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # press 'q' to quit
        break
    
cap.release()
cv2.destroyAllWindows