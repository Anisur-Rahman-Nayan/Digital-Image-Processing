import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)
def rotate(img,angle,center=None):
    width = img.shape[1]
    height = img.shape[0]
    if center is None:
        center = (width//2,height//2)
    rotMatrix = cv.getRotationMatrix2D(center,angle,scale=1)
    dim = (width,height)
    return cv.warpAffine(img,rotMatrix,dim)
rotated = rotate(img,90)
cv.imshow('rotated', rotated)
rotated2 = rotate(rotated,90)
cv.imshow('rotated2', rotated2)
flip = cv.flip(img,-1)
cv.imshow('flipped',flip)
cv.waitKey(0)