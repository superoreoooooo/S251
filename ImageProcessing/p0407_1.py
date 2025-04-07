import numpy as np
import cv2
from p0407_0 import filter

img = cv2.imread('ImageProcessing/images_chap7/filter_sharpen.jpg', cv2.IMREAD_GRAYSCALE)

data1 = [    0, -1,  0,
            -1,  5, -1,
             0, -1,  0  ]

data2 = [[  -1, -1, -1,
            -1,  9, -1,
            -1, -1, -1   ]]

mask1 = np.array(data1, np.float32).reshape((3, 3))
mask2 = np.array(data2, np.float32)

sharpen1 = filter(img, mask1)
sharpen1 = cv2.convertScaleAbs(sharpen1)

sharpen2 = filter(img, mask2)
sharpen2 = cv2.convertScaleAbs(sharpen2)

cv2.imshow('img', img)
cv2.imshow('sharpen1', sharpen1)
cv2.imshow('sharpen2', sharpen2)
cv2.waitKey(0)