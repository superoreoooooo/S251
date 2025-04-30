import cv2
import numpy as np

def contain(p, shape) :
    return 0 <= p[0] < shape[0] and 0 < p[1] < shape[1]

def translate(img, pt) :
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]) :
        for j in range(img.shape[1]) :
            x, y = np.subtract((j, i), pt)
            if (contain((y, x), img.shape)) :
                dst[i, j] = img[y, x]
                
    return dst



img = cv2.imread('Imageprocessing/images_chap8/translate.jpg', cv2.IMREAD_GRAYSCALE)

size = (350, 400)
dst1 = translate(img, (30, 80))
dst2 = translate(img, (-70, -50))

cv2.imshow("img", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)