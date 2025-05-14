import cv2
import time
import numpy as np
from Common.dft2d import dft, idft, calc_spectrum, fftshift

img = cv2.imread("ImageProcessing/images_chap9/dft_240.jpg", cv2.IMREAD_GRAYSCALE)

def dft2(img) :
    tmp = [dft(row) for row in img]
    dst = [dft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def idft2(img) :
    tmp = [idft(row) for row in img]
    dst = [idft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ck_time(mode=0) :
    global stime
    if (mode == 0) :
        stime = time.perf_counter()
    elif (mode == 1) :
        etime = time.perf_counter()
        print(f"eta : {etime - stime}")
    
ck_time(0)
dft = dft2(img)
spec1 = calc_spectrum(dft)
spec2 = fftshift(spec1)
idft = idft2(dft).real
ck_time(1)

ck_time(0)
fft = np.fft.fft2(img)
spec3 = calc_spectrum(fft)
spec4 = fftshift(spec2)
ck_time(1)

cv2.imshow("img", img)
cv2.imshow("spec1", spec1)
cv2.imshow("spec2", spec2)
cv2.imshow("spec3", spec3)
cv2.imshow("spec4", spec4)
cv2.imshow("idft img", cv2.convertScaleAbs(idft))

cv2.waitKey(0)