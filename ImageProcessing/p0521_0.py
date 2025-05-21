import cv2
import numpy as np
from Common.utils import put_string

def cornerHarris(img, ksize, k) :
    dx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize)
    dy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize)
    
    a = cv2.GaussianBlur(dx * dx, (5, 5), 0)
    b = cv2.GaussianBlur(dy * dy, (5, 5), 0)
    c = cv2.GaussianBlur(dx * dy, (5, 5), 0)
    
    corner = (a * b - c ** 2) - k * (a + b) ** 2
    
    return corner

def drawCorner(corner, img, thresh) :
    corner = cv2.normalize(corner, 0, 300, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    pts = np.where(corner > thresh)
    h, w = corner.shape
    corners = []
    
    for j, i in np.transpose(pts) :
        if (0 < i < h - 1) and (0 < j < w - 1) :
            neighbor = corner[i-1:i+2, j-1:j+2].flatten()
            max = np.max(neighbor[1::2])
            if (corner[i, j] >= max) : corners.append((j, i))
            
    for pt in corners :
        cv2.circle(img, pt, 3, (0, 230, 0), -1)
    
    return img

def onCornerHarris(thresh) :
    img1 = drawCorner(corner1, np.copy(img), thresh)
    img2 = drawCorner(corner2, np.copy(img), thresh)
    
    put_string(img1, "USER", (10, 30), "")
    put_string(img2, "OpenCV", (10, 30), "")
    
    dst = cv2.repeat(img1, 1, 2)
    dst[:, img1.shape[1]:, :] = img2
    cv2.imshow("harris", dst)

img = cv2.imread("ImageProcessing/images_chap9/fft_300.jpg", cv2.IMREAD_COLOR)

blocksize = 4
apSize = 3
k = 0.04
thresh = 2
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corner1 = cornerHarris(gray, apSize, k)
corner2 = cv2.cornerHarris(gray, blocksize, apSize, k)

onCornerHarris(thresh)
cv2.createTrackbar("threshold", "harris", thresh, 20, onCornerHarris)
cv2.waitKey(0)