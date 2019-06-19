import cv2
from matplotlib import pyplot as plt
import numpy as np
cv2.namedWindow('window',flags=cv2.WINDOW_NORMAL)


paint= cv2.imread('paint.jpg')
logo=cv2.imread('karaiskos.jpg')

logo_gray= cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

ret, our_mask= cv2.threshold(logo_gray, 190, 255, cv2.THRESH_BINARY_INV)
our_mask_inv= cv2.bitwise_not(our_mask)

rows, cols, channels= logo.shape
paint_crop= paint[0:rows, 0:cols]

magic= cv2.bitwise_and(logo, logo, mask=our_mask)
magic2= cv2.bitwise_and(paint_crop, paint_crop, mask=our_mask_inv)

part_final= cv2.add(magic, magic2)

paint[0:rows, 0:cols]= part_final

cv2.imshow('window',paint)
cv2.waitKey(0)
cv2.destroyAllWindows()