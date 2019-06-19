'''
This program will use the python opencv logo to show an example of image thresholding/mask
and use the same logo to paste it on an third image.
This program was designed in Pycharm IDE.
by Christianidis Vasileios
email: basilisvirus@hotmail.com

'''

import cv2
from matplotlib import pyplot as plt
import numpy as np
cv2.namedWindow('window',flags=cv2.WINDOW_NORMAL)

paint= cv2.imread('paint.jpg')
logo=cv2.imread('opencv.jpg')

#grayscale the logo
logo_gray= cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

#make a mask, where if pixelVal>12, then paint it 255 (which is white)
ret, mask= cv2.threshold(logo_gray, 12, 255, cv2.THRESH_BINARY_INV)

#cropping the paint
rows, cols, channels= logo.shape
crop_paint= paint[0:rows, 0:cols]

#blending the images
magic= cv2.bitwise_and(crop_paint, crop_paint, mask=mask)

final_theme= cv2.add(logo, magic)

#showtime
paint[0:rows, 0:cols]=final_theme

cv2.imshow('window',paint)

cv2.waitKey(0)
cv2.destroyAllWindows()