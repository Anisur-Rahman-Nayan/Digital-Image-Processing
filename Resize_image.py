import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# let's downscale the image using new  width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv.resize(img, down_points, interpolation=cv.INTER_LINEAR)

# let's upscale the image using new  width and height
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv.resize(img, up_points, interpolation=cv.INTER_LINEAR)

# Display images
cv.imshow('Resized Down by defining height and width', resized_down)
cv.waitKey()
cv.imshow('Resized Up image by defining height and width', resized_up)
cv.waitKey()
# press any key to close the windows
cv.destroyAllWindows()


