import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)


cv.imshow("B", b)
cv.imshow("G", g)
cv.imshow("R", r)


blue = cv.merge([b, blank, blank])
green = cv.merge([b, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow("B", blue)
cv.imshow("G", green)
cv.imshow("R", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
cv.waitKey(0)
