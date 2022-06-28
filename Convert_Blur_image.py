import cv2 as cv

img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("original Img",img)

blur = cv.boxFilter(img, ksize=(3 ,3), ddepth=-1, anchor=(-1, -1))
cv.imshow('blur',blur)

cv.waitKey(0)
