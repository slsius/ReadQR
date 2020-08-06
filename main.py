from __future__ import print_function
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image
import numpy as np
import cv2
from builtins import input
import cv2 as cv

# Image path 
#image_path = '/Users/siu/Documents/PythonPrograms/ReadQR/qr.jpeg'
image_path = 'qr.jpeg'

rt = 0.8

img = cv2.imread(image_path,0)
#image = img 

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

bw_im = thresh1
barcodes = decode(bw_im, symbols=[ZBarSymbol.QRCODE])
image = thresh1

new_image = np.zeros(image.shape, image.dtype)
alpha = 1.0 # Simple contrast control
beta = 0    # Simple brightness control
# Initialize values
'''
print(' Basic Linear Transforms ')
print('-------------------------')
try:
    alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
    beta = int(input('* Enter the beta value [0-100]: '))
except ValueError:
    print('Error, not a number')
'''    
# Do the operation new_image(i,j) = alpha*image(i,j) + beta
# Instead of these 'for' loops we could have used simply:
# new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
# but we wanted to show you how to access the pixels :)
'''
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
cv.imshow('Original Image', image)
cv.imshow('New Image', new_image)
# Wait until user press some key
cv.waitKey()
cv2.destroyAllWindows()
'''

rgb_planes = cv2.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)

cv2.imwrite('shadows_out.png', result)
cv2.imwrite('shadows_out_norm.png', result_norm)




bw_im = tresult_planes
barcodes = decode(bw_im, symbols=[ZBarSymbol.QRCODE])
image = result_planes

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
cv2.destroyAllWindows()

