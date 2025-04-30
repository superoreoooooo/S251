import cv2
import numpy as np
import time

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]
    
    return dst

def scaling2(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)
            dst[i, j] = img[y, x]
    return dst

def time_check(func, img, size, title) :
    start_time = time.perf_counter()
    ret_img = func(img, size)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(title, "eta = %0.2f ms" % elapsed)
    return ret_img


img = cv2.imread('Imageprocessing/images_chap8/scaling.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = time_check(scaling, img, (300, 400), "type1")
dst2 = time_check(scaling2, img, (300, 400), "type2")

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)