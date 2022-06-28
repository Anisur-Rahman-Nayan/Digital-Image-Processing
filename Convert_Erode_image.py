import cv2 as cv
img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("Original img",img)

gaussian = cv.GaussianBlur(img, ksize=(3,3), sigmaX=0)
# cv.imshow("Gaussian", gaussian)

canny_gaussian = cv.Canny(gaussian, 125, 175)
# cv.imshow("Canny On Gaussian", canny_gaussian)

dilated = cv.dilate(canny_gaussian,(3,3))
cv.imshow('dilated', dilated)

eroded = cv.erode(dilated,(7,7))
cv.imshow('eroded',eroded)

cv.waitKey(0)

cv.waitKey(0)