import cv2
import numpy as np
from matplotlib import pyplot as plt

# Image path 
#image_path = '/Users/siu/Documents/PythonPrograms/ReadQR/qr.jpeg'
image_path = 'qr.jpeg'

img = cv2.imread(image_path,0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('My Image', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()


ret,thresh1 = cv2.threshold(erosion,127,255,cv2.THRESH_BINARY)
cv2.imshow('My Image', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
ret,thresh4 = cv2.threshold(erosion,127,255,cv2.THRESH_TOZERO)
cv2.imshow('My Image', thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
