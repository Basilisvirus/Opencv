'''
This sketch will use your camera to display to a new window
only the red and blue colors of the video frames.

Created by Christianidis Vasileios
email: basilisvirus@hotmail.com

'''


import cv2
import numpy as np

#change the x in VideoCapture(x) to change the camera you are using
#bind the camera
cap = cv2.VideoCapture(0)
#creating new resizable window
cv2.namedWindow('window', flags= cv2.WINDOW_NORMAL)

while(1):
    #take each frame
    ret, frame= cap.read()
    #convert
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #blue
    lower_blue = np.array([90, 50, 10])
    upper_blue = np.array([130, 255, 255])
    mask_blue= cv2.inRange(hsv, lower_blue, upper_blue)

    #red
    lower_red= np.array([0,131,10])
    upper_red= np.array([7,255,255])
    mask_red= cv2.inRange(hsv, lower_red, upper_red)

    #common mask
    common_mask= cv2.bitwise_or(mask_blue, mask_red)

    #finalize
    final= cv2.bitwise_and(frame, frame, mask= common_mask)

    cv2.imshow('window',final)
    cv2.waitKey(1)