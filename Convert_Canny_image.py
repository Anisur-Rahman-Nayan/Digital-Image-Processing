import cv2 as cv
img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("Original img",img)

canny = cv.Canny(img,125,175)
cv.imshow("Canny",canny)

cv.waitKey(0)