import cv2 as cv
img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("Original img",img)

gaussian = cv.GaussianBlur(img, ksize=(3,3), sigmaX=0)
cv.imshow("Gaussian Blur", gaussian)

cv.waitKey(0)