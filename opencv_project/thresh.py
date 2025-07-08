import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRay', gray)

#simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threashold', thresh)



cv.waitKey(0)