

import cv2 as cv
import numpy as np


# Load the input image
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Original', img)

# Use the cvtColor() function to grayscale the image
LAB_image = cv.cvtColor(img, cv.COLOR_BGR2LAB)

cv.imshow('LAB image', LAB_image)
cv.waitKey(0)

cv.destroyAllWindows()