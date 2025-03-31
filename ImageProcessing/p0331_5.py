import cv2
import numpy as np
from p0331_3 import draw

img = cv2.imread("ImageProcessing/images_chap6/equalize.jpg", cv2.IMREAD_GRAYSCALE)

bins, ranges = [256], [0, 256]

hist = cv2.calcHist([img], [0], None, bins, ranges)

accum_hist = np.zeros(hist.shape[:2], np.float32)
accum_hist[0] = hist[0]
for i in range(1, hist.shape[0]) :
    accum_hist[i] = accum_hist[i - 1] + hist[i]

accum_hist = (accum_hist / sum(hist)) * 255

dst1 = [[accum_hist[val] for val in row] for row in img]
dst1 = np.array(dst1, np.uint8)

dst2 = cv2.equalizeHist(img)
hist1 = cv2.calcHist([dst1], [0], None, bins, ranges)
hist2 = cv2.calcHist([dst2], [0], None, bins, ranges)
hist_img = draw(hist)
hist_img1 = draw(hist1)
hist_img2 = draw(hist2)

print(hist1.shape)

cv2.imshow("img", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("hist", hist)
cv2.imshow("hist1", hist1)
cv2.imshow("hist2", hist2)

cv2.waitKey(0)