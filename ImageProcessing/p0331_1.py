import cv2
import numpy as np

img = cv2.imread("ImageProcessing/images_chap6/pixel.jpg", cv2.IMREAD_GRAYSCALE)

(x, y), (w, h) = (180, 37), (15, 10)

roi_img = img[y : y + h, x : x + w]

print("roi = ")

for r in roi_img :
    for p in r :
        print("%4d" % p, end = " ")
    print()
print("\n")

cv2.rectangle(img, (x, y, w, h), 255, 1)
cv2.imshow("img", roi_img)

cv2.waitKey()