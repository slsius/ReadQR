from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image
import numpy as np
import cv2

# Image path 
#image_path = '/Users/siu/Documents/PythonPrograms/ReadQR/qr.jpeg'
image_path = 'qr.jpeg'

rt = 0.8

img = cv2.imread(image_path,0)
image = img 

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
bw_im = thresh1
barcodes = decode(bw_im, symbols=[ZBarSymbol.QRCODE])

# loop over the detected barcodes
for barcode in barcodes:
    # extract the bounding box location of the barcode and draw the
    # bounding box surrounding the barcode on the image
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # the barcode data is a bytes object so if we want to draw it on
    # our output image we need to convert it to a string first
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    # draw the barcode data and barcode type on the image
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 2)
    # print the barcode type and data to the terminal
    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
# show the output image


imS = cv2.resize(image, (int(image.shape[1]*rt), int(image.shape[0]*rt)))
cv2.imshow("product", imS)
cv2.imwrite('product.jpg',image)

cv2.waitKey(0)
