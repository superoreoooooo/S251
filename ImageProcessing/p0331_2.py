import cv2
import numpy as np

img1 = cv2.imread("ImageProcessing/Images_chap6/add1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("ImageProcessing/Images_chap6/add2.jpg", cv2.IMREAD_GRAYSCALE)

alpha, beta = 0.6, 0.7

add1 = cv2.add(img1, img2)
add2 = cv2.add(img1 * alpha, img2 * beta)
add2 = np.clip(add2, 0, 255).astype(np.uint8)
add3 = cv2.addWeighted(img1, alpha, img2, beta, 0)

titles = ['img1', 'img2', 'add1', 'add2', 'add3']

for t in titles :
    cv2.imshow(t, eval(t))

cv2.waitKey(0)