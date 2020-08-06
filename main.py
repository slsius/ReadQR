from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image
import numpy as np
import cv2

rt = 0.15


image = cv2.imread(
    'wiki.png')

cv2.imwrite('original.jpg',image)

imageGRY = cv2.imread(
    'wiki.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('gray.jpg',imageGRY)

blur = cv2.GaussianBlur(imageGRY, (5, 5), 0)
cv2.imwrite('blur.jpg',blur)

ret, bw_im = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# zbar
cv2.imshow("bw_im", cv2.resize(
    bw_im, (int(bw_im.shape[1]*rt), int(bw_im.shape[0]*rt))))

cv2.imwrite('bw_im.jpg',bw_im)

bw_im = cv2.imread(
    'wiki.png')
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
