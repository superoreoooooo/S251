import numpy as np
import cv2

def nonmax_suppression(sobel, direct) :
    r, c = sobel.shape[:2]
    dst = np.zeros((r, c), np.float32)

    for i in range(1, r - 1) :
        for j in range(1, c - 1) :
            values = sobel[i-1 : i+2, j-1 : j+2].flatten()
            first = [3, 0, 1 ,2]
            id = first[direct[i, j]]
            v1, v2 = values[id], values[8 - id]

            dst[i, j] = sobel[i, j] if (v1 < sobel[i, j] > v2) else 0

    return dst

def trace(max_sobel, i, j, low) :
    h, w = max_sobel.shape
    if (0 <= i < h and 0 <= j < w) == False :
        return
    if (pos_ck[i, j] == 0 and max_sobel[i, j] > low) :
        pos_ck[i, j] = 255
        canny[i, j] = 255

        trace(max_sobel, i - 1, j - 1, low)
        trace(max_sobel, i,     j - 1, low)
        trace(max_sobel, i + 1, j - 1, low)
        trace(max_sobel, i - 1, j    , low)
        trace(max_sobel, i + 1, j    , low)
        trace(max_sobel, i - 1, j + 1, low)
        trace(max_sobel, i,     j + 1, low)
        trace(max_sobel, i + 1, j + 1, low)

def hysteresis_th(max_sobel, low, high) :
    r, c = max_sobel.shape[:2]
    for i in range(1, r - 1) :
        for j in range(1, c - 1) :
            if (max_sobel[i, j] > high) :
                trace(max_sobel, i, j, low)

if __name__ == "__main__" :
    img = cv2.imread('ImageProcessing/images_chap7/canny.jpg', cv2.IMREAD_GRAYSCALE)
    pos_ck = np.zeros(img.shape[:2], np.uint8)
    canny = np.zeros(img.shape[:2], np.uint8)

    gaus_img = cv2.GaussianBlur(img, (5, 5), 0.3)
    Gx = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 1, 0, 3)
    Gy = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 0, 1, 3)
    sobel = cv2.magnitude(Gx, Gy)
    
    directs = cv2.phase(Gx, Gy) / (np.pi / 4)
    directs = directs.astype(np.int8) % 4
    max_sobel = nonmax_suppression(sobel, directs)
    hysteresis_th(max_sobel, 100, 150)

    canny2 = cv2.Canny(img, 100, 150)

    cv2.imshow('img', img)
    cv2.imshow('canny', canny)
    cv2.imshow('canny2', canny2)
    cv2.waitKey(0)