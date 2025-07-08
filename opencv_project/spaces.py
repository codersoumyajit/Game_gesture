import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show()



#BGR TO HSV/////
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR TO L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


plt.imshow(rgb)
plt.show()

cv.waitKey(0)