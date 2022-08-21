import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/group 1.jpg")
cv.imshow('group image',img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')
circle = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2),150,255,-1)
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle_masked = cv.bitwise_and(img,img,mask = circle)
rectangle_masked = cv.bitwise_and(img,img,mask = rectangle)
cv.imshow("Circle masked",circle_masked)
cv.imshow("Rectangle masked", rectangle_masked)
cv.waitKey(0)


# import cv2 as cv
# import numpy as np
#
# img = cv.imread("images.jfif")
# cv.imshow('cats',img)
#
# blank = np.zeros(img.shape[:2], dtype= 'uint8')
# blank = cv.merge([blank,blank,blank])
# circle = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2),150,(255,255,255),-1)
# rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),(255,255,255),-1)
#
# circle_masked = cv.bitwise_and(img,circle)
# rectangle_masked = cv.bitwise_and(img, rectangle)
# cv.imshow("Circle masked",circle_masked)
# cv.imshow("Rectangle masked", rectangle_masked)
# print(img.shape)
# cv.waitKey(0)


