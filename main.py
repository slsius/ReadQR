import cv2
import numpy as np
from matplotlib import pyplot as plt

# Image path 
#image_path = '/Users/siu/Documents/PythonPrograms/ReadQR/qr.jpeg'
image_path = 'qr.jpeg'

img = cv2.imread(image_path,0)
cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('My Image', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('My Image', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv2.imshow('My Image', thresh3)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow('My Image', thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('My Image', thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()







cv2.waitKey(0)
cv2.destroyAllWindows()
