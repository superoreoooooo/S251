import numpy as np
import cv2

def filter(img, mask) :
    r, c = img.shape[:2]
    dst = np.zeros((r, c), np.float32)
    yc, xc = mask.shape[0]//2 , mask.shape[1]//2

    for i in range(yc, r - yc) :
        for j in range(xc, c - xc) :
            y1, y2 = i - yc, i + yc + 1
            x1, x2 = j - xc, j + xc + 1
            roi = img[y1:y2, x1:x2].astype(np.float32)
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]

    return dst

if __name__ == "__main__" :
    img = cv2.imread('ImageProcessing/images_chap7/filter_blur.jpg', cv2.IMREAD_GRAYSCALE)

    data = [1 / 9, 1 / 9, 1 / 9,
            1 / 9, 1 / 9, 1 / 9,
            1 / 9, 1 / 9, 1 / 9]

    mask = np.array(data, np.float32).reshape((3, 3))
    blur1 = filter(img, mask)
    blur1 = blur1.astype(np.uint8)

    cv2.imshow('img', img)
    cv2.imshow('blur1', blur1)
    cv2.waitKey(0)