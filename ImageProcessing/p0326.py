import cv2
import numpy as np

img1 = cv2.imread("ImageProcessing/images_chap5/abs_test1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("ImageProcessing/images_chap5/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)

difimg1 = cv2.subtract(img1, img2)
difimg2 = cv2.subtract(np.int16(img1), np.int16(img2))
absdif1 = np.absolute(difimg2).astype('uint8')
absdif2 = cv2.absdiff(img1, img2)

x, y, w, h = 100, 150, 7, 3

print(difimg1[y:y+h, x:x+w])
print(difimg2[y:y+h, x:x+w])
print(absdif1[y:y+h, x:x+w])
print(absdif2[y:y+h, x:x+w])

titles = ['img1', 'img2', 'difimg1', 'absdif1', 'absdif2']
for t in titles :
    cv2.imshow(t, eval(t))
cv2.waitKey(0)