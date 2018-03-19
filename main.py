import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()