import cv2
import numpy as np


img = cv2.imread('ImageProcessing/images_chap5/bit_test.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('ImageProcessing/images_chap5/logo.jpg', cv2.IMREAD_COLOR)

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H, W), (h, w) = img.shape[:2], logo.shape[:2]
x, y = (W-w)//2, (H-h)//2   
roi = img[y:y+h, x:x+w]

fg = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
bg = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

dst = cv2.add(bg, fg)
img[y:y+h, x:x+w] = dst

cv2.imshow('fg', fg)
cv2.imshow('bg', bg)
cv2.imshow('dst', dst)
cv2.imshow('img', img)

cv2.waitKey(0)