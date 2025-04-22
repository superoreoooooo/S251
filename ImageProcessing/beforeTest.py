import numpy as np
import matplotlib.pyplot as plt
import cv2
import os


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
#예제 2?
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


