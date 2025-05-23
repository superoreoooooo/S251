import numpy as np
import cv2
from Common.interpolation import rotate_pt

def calc_angle(pts) :
    d1 = np.subtract(pts[1], pts[0]).astype(float)
    d2 = np.subtract(pts[2], pts[0]).astype(float)
    
    angle1 = cv2.fastAtan2(d1[1], d1[0])
    angle2 = cv2.fastAtan2(d2[1], d2[0])
    
    return (angle2 - angle1)

def draw_point(x, y) :
    pts.append([x, y])
    print("point : ", len(pts), [x, y])
    cv2.circle(tmp, (x, y), 2, 255, 2)
    cv2.imshow("img", img)
    
def onMouse(event, x, y, flags, param) :
    global tmp, pts
    if (event == cv2.EVENT_LBUTTONUP and len(pts) == 0) : draw_point(x, y)
    if (event == cv2.EVENT_LBUTTONDOWN and len(pts) == 1) : draw_point(x, y)
    if (event == cv2.EVENT_LBUTTONUP and len(pts) == 2) : draw_point(x, y)
    
    if (len(pts) == 3) :
        angle = calc_angle(pts)
        dst = rotate_pt(img, angle, pts[0])
        cv2.imshow("img", dst)
        tmp = np.copy(img)
        pts = []
        
img = cv2.imread("Imageprocessing/images_chap8/rotate.jpg", cv2.IMREAD_GRAYSCALE)
tmp = np.copy(img)
pts = []

cv2.imshow("img", img)
cv2.setMouseCallback("img", onMouse, 0)
cv2.waitKey(0)