import cv2
import numpy as np

img = cv2.imread('ImageProcessing/images_chap5/sum_test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("a", img)  

img = cv2.sort(img, cv2.SORT_EVERY_ROW)

cv2.imshow("img", img)
cv2.waitKey(0)