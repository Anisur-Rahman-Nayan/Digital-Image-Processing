import numpy as np
import cv2 as cv
img = cv.imread('Resources/Photos/sudoku.png')
cv.imshow('Original Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Sudoku in Gray', gray)

laplacian = cv.Laplacian(gray, cv.CV_64F)
cv.imshow("Sudoku in laplacian",laplacian)

lap = np.uint8(np.absolute(laplacian))
cv.imshow('Sudoku in lap', lap)

sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobelx',sobelx)
cv.imshow('Sobely', sobely)
cv.imshow("Combined",combined)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
combine_d = np.uint8(np.absolute(cv.bitwise_or(sobelx,sobely)))


cv.imshow('Sobel_X',sobelx)
cv.imshow("Sobel_Y",sobely)
cv.imshow('Combine_d',combine_d)


cv.waitKey(0)