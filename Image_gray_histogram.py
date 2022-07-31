import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Nature', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)

# hist= cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("gray histogram")
plt.xlabel("pixel Intensity")
plt.ylabel("number of pixel")

blue_hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(blue_hist,color='blue')

red_hist = cv.calcHist([img],[2],None,[256],[0,256])
plt.plot(red_hist,color='red')

green_hist = cv.calcHist([img],[1],None,[256],[0,256])
plt.plot(green_hist,color='green')

# plt.plot(hist,color='black')
plt.xlim([0,256])
plt.show()

# cv.imshow('hist',hist)

cv.waitKey(0)