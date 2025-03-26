import cv2
import numpy as np

img = cv2.imread('ImageProcessing/images_chap5/minMax.jpg', cv2.IMREAD_GRAYSCALE)

minVal, maxVal, _, _ = cv2.minMaxLoc(img)

ratio = 255 / (maxVal - minVal)
dst = np.round((img - minVal) * ratio).astype('uint8')
minDst, maxDst, _, _ = cv2.minMaxLoc(dst)

print(f"minVal = {minVal}, maxVal = {maxVal}")
print(f"minDst = {minDst}, maxDst = {maxDst}")

cv2.imshow('img', img)
cv2.imshow('dst', dst)  
cv2.waitKey(0)