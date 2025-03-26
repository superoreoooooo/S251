import cv2
import numpy as np

img = cv2.imread('ImageProcessing/images_chap5/color.jpg', cv2.IMREAD_COLOR)

bgr = cv2.split(img)
print(f"{type(bgr[0])} {len(bgr[0])} {bgr[0].shape}")
b = np.zeros((360, 480, 3), np.uint8)
b[:, :, 0] = bgr[0]
g = np.zeros((360, 480, 3), np.uint8)
g[:, :, 1] = bgr[1]
r = np.zeros((360, 480, 3), np.uint8)
r[:, :, 2] = bgr[2]

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

cv2.waitKey(0)