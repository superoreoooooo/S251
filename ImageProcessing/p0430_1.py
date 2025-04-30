import cv2
import numpy as np
import time

def blinear(img, pt) :
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x - 1                
    if y >= img.shape[0]-1: y = y - 1
    
    P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten())
    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3 - P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    
    return np.clip(P, 0, 255)

def scaling_blinear(img, size) :
    rY, rX = np.divide(size[::-1], img.shape[:2])
    
    dst = [
        [
            blinear(img, (j / rX, i / rY)) 
            for j in range(size[0])
            ] 
           for i in range(size[1])
           ]
    
    return np.array(dst, img.dtype)


img = cv2.imread('Imageprocessing/images_chap8/scaling.jpg', cv2.IMREAD_GRAYSCALE)

size = (350, 400)
dst1 = scaling_blinear(img, size)
dst2 = cv2.resize(img, size, 0, 0, cv2.INTER_LINEAR)

cv2.imshow("img", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)