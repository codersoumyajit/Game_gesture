import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#blur an image #odd no for blur img(3,3) or (7,7 for more blur)
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#Edge Cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edge', canny)

#Dilating th iamges
# dilated=cv.dilate(canny, (3,3), iterations =2)
# cv.imshow('Dilated', dilated)

#eroding
# eroded = cv.erode(dilated,(3,3), iterations=1)
# cv.imshow('Eroded',eroded)

#Resize
# resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)