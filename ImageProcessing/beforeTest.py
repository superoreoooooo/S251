import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

#4
"""
print(os.getcwd())
a = cv2.imread("ImageProcessing/images_chap4/read_gray.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("a", a)
b = cv2.waitKey(0)
print(b)
cv2.destroyAllWindows()

"""

"""
def onMouse(event, x, y, flags, param) :
    if (event == cv2.EVENT_LBUTTONDOWN) :
        print("left click")
    elif (event == cv2.EVENT_RBUTTONDOWN) :
        print("right click")

img = np.full((200, 300), 255, np.uint8)
cv2.imshow("a", img)
cv2.setMouseCallback("a", onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

"""
img = np.full((300, 300, 3), 255, np.uint8)
cv2.line(img, (50, 50), (250, 250), (255, 0, 0), 3)
cv2.line(img, (250, 50), (50, 250), (0, 0, 255), 3)
cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

"""
img = np.full((1000, 1000, 3), 255, np.uint8)

sPos = tuple()

def onMouse(event, x, y, flags, param) :
    if (event == cv2.EVENT_RBUTTONDOWN) :
        global sPos
        sPos = (x, y)
    if (event == cv2.EVENT_RBUTTONUP) :
        ePos = (x, y)
        mPos = ((sPos[0] + ePos[0]) // 2, (sPos[1] + ePos[1]) // 2)
        radius = np.sqrt((sPos[0] - ePos[0]) ** 2 + (sPos[1] - ePos[1]) ** 2) / 2 if sPos[0] > ePos[0] else np.sqrt((sPos[1] - ePos[1]) ** 2 + (sPos[0] - ePos[0]) ** 2) / 2
        cv2.circle(img, mPos, int(radius), (255, 0, 0), 3)
        cv2.imshow("a", img)

cv2.imshow("a", img)
cv2.setMouseCallback("a", onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

"""
capture = cv2.VideoCapture(0)

while True :
    ret, frame = capture.read()
    if not ret : break
    if cv2.waitKey(30) >= 0 : break
    
    cv2.imshow("a", frame)
    
capture.release()
"""

# 5
"""
img = cv2.imread("test.png")
img = cv2.flip(img, -1)
#img = cv2.repeat(img, 2, 3)
img = cv2.hconcat([img, img]) #horizontal
img = cv2.vconcat([img, img]) #vertical

img = cv2.transpose(img)

cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

""" #split 후 merge로 한색만뜨게하기
img = cv2.imread("ImageProcessing/images_chap5/color.jpg")
img = cv2.split(img)

print(img[0].shape)
print(np.zeros(img[0].shape, np.uint8).shape)
img = cv2.merge([np.zeros(img[0].shape, np.uint8), np.zeros(img[0].shape, np.uint8), img[2]]) 

print(img)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

img = cv2.imread("ImageProcessing/images_chap5/bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("ImageProcessing/images_chap5/logo.jpg", cv2.IMREAD_COLOR)

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H, W), (h, w) = img.shape[:2], logo.shape[:2]
x, y = (W - w) // 2, (H - h) // 2
roi = img[y : y + h, x : x + w]

fg = cv2.bitwise_and(logo, logo, mask = fg_pass_mask)
bg = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

dst = cv2.add(bg, fg)
img[y : y + h, x : x + w] = dst

cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()