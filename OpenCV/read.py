import cv2 as cv

##reading and showing image from local
img = cv.imread('Photos/cat.png')

cv.imshow('Cat',img)

##dimension 
h, w = img.shape[:2]
print(f'height {h}, width {w}')


##img if img is larger than screen wont get displayed fully

cv.waitKey(0)