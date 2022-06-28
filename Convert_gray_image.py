
import cv2 as cv

img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow('Original img ',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


cv.waitKey(0)