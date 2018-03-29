import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys, os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
#bike_cascade = cv2.CascadeClassifier('bicycle.xml')

try:
    cap = cv2.VideoCapture(0)
    fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
    #vid = cv2.VideoWriter(['output.mp4',fourcc, 25, (640,480), False])
    vid = cv2.VideoWriter('outpy.avi',fourcc, 10, (640,480))
    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
        #bikes = bike_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
        	cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        	#roi_gray = gray[y:y+h, x:x+w] #region of image
        	#roi_color = frame[y:y+h, x:x+w]
        	#eyes = ...(roi_gray)

        # bodies = body_cascade.detectMultiScale(gray)
        # for (x,y,w,h) in bodies:
        # 	cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

        #for (x,y,w,h) in bikes:
        #	cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow('frame',frame)
        #vid.write(frame)

except KeyboardInterrupt:
    print 'yo'
    cap.release()
    cv2.destroyAllWindows()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
