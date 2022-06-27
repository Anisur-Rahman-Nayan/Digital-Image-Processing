import cv2 as cv
import numpy as np

img = np.zeros((500,500,3),dtype="uint8")
# img.fill(255)
img[:] = 255,255,255
img[160:340,100:400] = 78, 106, 00

cv.rectangle(img, (100, 160), (400, 340), (0, 0, 0),thickness=3)
cv.circle(img, (235, 250), 60, (65, 42, 244), thickness=-1)
cv.line(img, (95, 155), (98, 499), thickness=7, color=(0, 0, 0))


cv.imshow('blank',img)
cv.waitKey(0)