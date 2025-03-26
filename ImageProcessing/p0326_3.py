import cv2
import numpy as np

img = cv2.imread('ImageProcessing/images_chap5/sum_test.jpg', cv2.IMREAD_COLOR)

mask = np.zeros(img.shape[:2], np.uint8)
mask[60:160, 20:120] = 255

sumVal = cv2.sumElems(img)
meanVal1 = cv2.mean(img)
meanVal2 = cv2.mean(img, mask)

print(f"\n\nsumVal = {sumVal}")
print(f"meanVal1 = {meanVal1}")
print(f"meanVal2 = {meanVal2}\n\n")

mean, stddev = cv2.meanStdDev(img)
mean2, stddev2 = cv2.meanStdDev(img, mask=mask)

print(f"mean = {mean.flatten()}\nstddev = {stddev.flatten()}")
print(f"mean2 = {mean2.flatten()}\nstddev2 = {stddev2.flatten()}\n\n")

cv2.imshow('img', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)