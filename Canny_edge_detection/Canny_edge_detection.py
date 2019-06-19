'''
This sketch utilizes opencv and canny edge detection algorithm to find (visually)
edges in pictures. You change the input image if you want, and adjust the blur and the values of the
algorithm to see the edges.
Created by Christianidis Vasileios
email: basilisvirus@hotmail.com
'''


import cv2


def nothing(x):
    pass

img= cv2.imread('dave.jpg')

cols, rows= img.shape[:2]

if cols < rows:
    min= int(cols*(1/100))
else:
    min= int(rows*(1/100))

if min<190:
    min=190

cv2.namedWindow('trackbar', flags=cv2.WINDOW_NORMAL)
cv2.namedWindow('img', flags=cv2.WINDOW_NORMAL)
cv2.createTrackbar('high range', 'trackbar', 0, min, nothing)
cv2.createTrackbar('low range', 'trackbar', 0, min, nothing)
cv2.createTrackbar('blur', 'trackbar', 1, 31, nothing)

while(True):
    low_r= cv2.getTrackbarPos('high range', 'trackbar')
    high_r= cv2.getTrackbarPos('low range', 'trackbar')
    blur= cv2.getTrackbarPos('blur', 'trackbar')
    if blur==0:
        blur=1
    img_blur = cv2.blur(img, (blur, blur))
    edges= cv2.Canny(img_blur, low_r, high_r)
    cv2.imshow('img', edges)
    cv2.waitKey(2)


cv2.waitKey(0)
cv2.destroyAllWindows()