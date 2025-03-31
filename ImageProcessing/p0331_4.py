import cv2
import numpy as np
from p0331_3 import draw

def search(hist, bias = 0) :
    for i in range(hist.shape[0]) :
        idx = np.abs(bias - i)
        if hist[idx] > 0 :
            return idx
    return -1

img = cv2.imread("ImageProcessing/images_chap6/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)

bsize, ranges = [64], [0, 256]

hist = cv2.calcHist([img], [0], None, bsize, ranges)

bin_width = ranges[1] / bsize[0]

low = search(hist, 0) * bin_width
high = search(hist, bsize[0] - 1) * bin_width

idx = np.arange(0, 256)
idx = (idx - low) / (high - low) * 255
idx[0:int(low)] = 0
idx[int(high + 1):] = 255

dst = cv2.LUT(img, idx.astype('uint8'))

hist_dst = cv2.calcHist([dst], [0], None, bsize, ranges)
hist_img = draw(hist, (200, 360))
hist_dst_img = draw(hist_dst, (200, 360))

print(hist.shape)


cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.imshow("hist_img", hist_img)
cv2.imshow("hist_dst_img", hist_dst_img)
cv2.waitKey(0)