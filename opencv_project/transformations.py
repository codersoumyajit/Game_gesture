import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x ---> left
#-y ----> up
# x ----> right
# y---> down

translated = translate(img, 100,100)
cv.imshow('Translated', translated)

resized = cv.resize(img, (500,500), interpolation =cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flip
flip= cv.flip(img, -1)
cv.imshow('Flip', flip)

#croping
cropped = img[200:400 , 300:400]
cv.imshow('cropped', cropped)



cv.waitKey(0)