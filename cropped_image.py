import cv2 as cv
img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("Original img",img)

cropped = img[50:400, 100:470]
cv.imshow("Cropped",cropped)

cv.waitKey(0)