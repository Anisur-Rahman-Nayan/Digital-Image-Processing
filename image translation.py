import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

def translate(img, x,y):
    width = img.shape[1]
    height = img.shape[0]
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dim = (width,height)
    return cv.warpAffine(img,transMatrix,dim)


translated = translate(img,100,100)
cv.imshow('translated', translated)


cv.waitKey(0)