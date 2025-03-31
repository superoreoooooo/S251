import cv2
import numpy as np
import time

def pixelAcc1(image) :
    img1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]) :
        for j in range(image.shape[1]) :
            pixel = image[i, j]
            img1[i, j] = 255 - pixel
    return img1

def pixelAcc2(image) :
    lut = [255 - i for i in range(256)]
    lut = np.array(lut, np.uint8)

    img3 = lut[image]

    return img3

def pixelAcc3(image) :
    img4 = cv2.subtract(255, image)

    return img4

def pixelAcc4(image) :
    img5 = 255 - image
    return img5

image = cv2.imread("ImageProcessing/images_chap6/bright.jpg", cv2.IMREAD_GRAYSCALE)

def time_check(func, msg) :
    start_time = time.perf_counter()
    ret_img = func(image)
    eta = (time.perf_counter() - start_time) * 1000
    print(msg, eta)
    return ret_img

img1 = time_check(pixelAcc1, "직접 접근")
img2 = time_check(pixelAcc2, "룩업테이블")
img3 = time_check(pixelAcc3, "openCV 함수")
img4 = time_check(pixelAcc4, "ndArray 연산")

cv2.imshow("image - original", image)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.waitKey(0)