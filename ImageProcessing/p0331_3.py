import numpy as np
import cv2

def draw(hist, shape = (800, 2560)) :
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0]

    for i, h in enumerate(hist) :
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img, 0)

if __name__ == "__main__" :
    image = cv2.imread("Imageprocessing/Images_chap6/pixel.jpg", cv2.IMREAD_GRAYSCALE)

    hist = cv2.calcHist([image], [0], None, [32], [0, 256])

    cv2.imshow("image", image)
    cv2.imshow("hist", draw(hist))
    cv2.waitKey(0)