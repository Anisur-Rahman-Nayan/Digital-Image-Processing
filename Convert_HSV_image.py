
import cv2 as cv
import numpy as np


# Load the input image
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Original', img)

# Use the cvtColor() function to grayscale the image
HSV_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('HSV image', HSV_image)
cv.waitKey(0)

cv.destroyAllWindows()