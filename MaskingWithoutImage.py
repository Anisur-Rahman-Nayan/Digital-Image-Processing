import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rectangle',rectangle)
cv.imshow('Circle',circle)

bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise_And',bit_and)

bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise_Or',bit_or)

bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise_Xor',bit_xor)

circle_bit_not = cv.bitwise_not(circle)
cv.imshow('Circle Bitwise_Not',circle_bit_not)

cv.waitKey(0)
