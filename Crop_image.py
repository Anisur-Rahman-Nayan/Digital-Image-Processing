import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

cropped = img[50:400, 100:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)

#
# import cv2 as cv
# img = cv.imread("Resources/Photos/cat.jpg")
# cv.imshow("Original img",img)
#
# cropped = img[50:400, 100:470]
# cv.imshow("Cropped",cropped)
#
# cv.waitKey(0)