import cv2

img = cv2.imread('ImageProcessing/images_chap5/flip_test.jpg', cv2.IMREAD_COLOR)

if img is None : raise Exception("영상파일 읽기 오류")  

x_axis = cv2.flip(img, 0)
y_axis = cv2.flip(img, 1)
xy_axis = cv2.flip(img, -1)
rep_img = cv2.repeat(img, 1, 2)
trans_img = cv2.transpose(img)

titles = ['img', 'x_axis', 'y_axis', 'xy_axis', 'rep_img', 'trans_img']

for t in titles:
    cv2.imshow(t, eval(t))

cv2.waitKey(0)