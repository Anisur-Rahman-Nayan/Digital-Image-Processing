# import cv2
# import numpy as np
#
# image = cv2.imread("Resources/Photos/park.jpg")
# image_norm = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
#
# cv2.imshow('original Image', image)
# cv2.imshow('Rotated Image', image_norm)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

image = cv2.imread("cat.jpg")

(h, w) = image.shape[:2]
center = (w / 2, h / 2)
angle = 30
scale = 1

M = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow('original Image', image)
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()