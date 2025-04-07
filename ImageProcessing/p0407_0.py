import numpy as np
import cv2

def filter(img, mask) :
    r, c = img.shape[:2]
    dst = np.zeros((r, c), np.uint8)
    yc, xc = mask.shape[0]//2 , mask.shape[1]//2

    for i in range(yc, r - yc) :
        for j in range(xc, c - xc) :
            y1, y2 = i - yc, i + yc + 1
            x1, x2 = j - xc, j + xc + 1
            roi = img[y1:y2, x1:x2]
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]

    return dst

img = cv2.imread('ImageProcessing/images_chap5/blur_test.jpg', cv2.IMREAD_COLOR)