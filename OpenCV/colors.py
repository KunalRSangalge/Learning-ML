import cv2 as cv

img = cv.imread('Photos/garden.png')
cv.imshow('garden',img)
#default -> BGR

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('garden gray',gray)

##HSV - huge sentration value
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv format',hsv)

# LAB or l*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab format',lab)
cv.waitKey(0)