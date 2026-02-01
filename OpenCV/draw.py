import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8') 
# cv.imshow('Blank',blank)


##painting img green
blank[200:300, 300:400] = 0,0,255
cv.imshow('red',blank)

#rectangle
cv.rectangle(blank,(0,0),(200,200),(0,255,255),thickness=cv.FILLED)

# cv.FILLED same as -1 
# dimensions can also given by blank.shape[0]//2 blank.shape[1]//2

cv.imshow('rectangle',blank)


##circle
cv.circle(blank,(200,200),radius=200,color=(0,239,222),thickness=3)
cv.imshow('circle',blank)

##text on img
cv.putText(blank,'Hello world',(255,255),cv.FONT_HERSHEY_TRIPLEX,color=(20,12,233),thickness=1,fontScale=1)
cv.imshow('text on img',blank)
cv.waitKey(0)