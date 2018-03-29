import cv2,sys, os, time
import numpy as np
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
uBody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
#bike_cascade = cv2.CascadeClassifier('bicycle.xml')

body_colors = []
face_colors = []

avg_body = np.zeros((300, 300, 3), np.uint8)
avg_face = np.zeros((300, 300, 3), np.uint8)

cap = cv2.VideoCapture(0)

try:
    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
        uBodies = uBody_cascade.detectMultiScale(gray, 1.3, 5)
        #bikes = bike_cascade.detectMultiScale(gray, 1.3, 5)

        for i,(x,y,w,h) in enumerate(faces):
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2) #BGR
            face = frame[y:y+h, x:x+w]
            face_avg_color_per_row = np.average(face, axis=0)
            face_avg_color = np.average(face_avg_color_per_row, axis=0)
            face_colors.append(face_avg_color)
            #roi_gray = gray[y:y+h, x:x+w] #region of image
        	#roi_color = frame[y:y+h, x:x+w]
        	#eyes = ...(roi_gray)

        for (x,y,w,h) in uBodies:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            body = frame[y:y+h, x:x+w]
            body_avg_color_per_row = np.average(body, axis=0)
            body_avg_color = np.average(body_avg_color_per_row, axis=0)
            body_colors.append(body_avg_color)

        #for (x,y,w,h) in bikes:
        #	cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow('frame',frame)

        avg_body[:] = np.average(body_colors,axis=0)
        avg_face[:] = np.average(face_colors,axis=0)
        cv2.imwrite('avg_body.jpg',avg_body)
        cv2.imwrite('avg_face.jpg',avg_face)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
    cap.release()
    cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
