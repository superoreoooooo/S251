import numpy as np
import cv2

from Common.utils import contain
from Common.interpolation import bilinear_value


def affine_transform(img, mat) :
    rows, cols = img.shape[:2] 
    inv_mat = cv2.invertAffineTransform(mat)
    
    pts = [np.dot(inv_mat, (j, i, 1)) for i in range(rows) for j in range(cols)]
    dst = [bilinear_value(img, p) if contain(p, size) else 0 for p in pts]
    dst = np.reshape(dst, (rows, cols)).astype('uint8')
    
    return dst


img = cv2.imread("imageprocessing/images_chap8/affine.jpg", cv2.IMREAD_GRAYSCALE)

center = (200, 200)
angle, scale = 30, 1
size = img.shape[::-1]

pt1 = np.array([(30, 70), (20, 240), (300, 110)], np.float32)
pt2 = np.array([(120, 20), (10, 180), (280, 260)], np.float32)

aff_mat = cv2.getAffineTransform(pt1, pt2)
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

dst1 = affine_transform(img, aff_mat)
dst2 = affine_transform(img, rot_mat)
dst3 = cv2.warpAffine(img, aff_mat, size, cv2.INTER_LINEAR)
dst4 = cv2.warpAffine(img, rot_mat, size, cv2.INTER_LINEAR)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
dst1 = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGR)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR)


for i in range(len(pt1)) :
    cv2.circle(img, tuple(pt1[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst1, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst3, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)
    

cv2.imshow("img", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.imshow("dst4", dst4)

cv2.waitKey(0)