import cv2
import numpy as np
from matplotlib import pyplot as plt

# Image path 
image_path = 'qr.jpeg '

img = cv2.imread(image_path,0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('My Image', thresh1)
cv2.imshow('My Image', thresh2)
cv2.imshow('My Image', thresh3)
cv2.imshow('My Image', thresh4)
cv2.imshow('My Image', thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
