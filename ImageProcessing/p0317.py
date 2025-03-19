import cv2
import numpy as np


"""
image = np.zeros((200, 300), np.uint8)
image.fill(255)

t1, t2 = "normal", "auto"
cv2.namedWindow(t1, cv2.WINDOW_NORMAL)
cv2.namedWindow(t2, cv2.WINDOW_AUTOSIZE)
cv2.imshow(t1, image)
cv2.imshow(t2, image)

cv2.resizeWindow(t1, 400, 300)
cv2.resizeWindow(t2, 400, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()"
"""

"""

switch_case = {
    ord('a'): "a",
    ord('b'): "b",
    0x41: "A",
    int('0x42', 16): "B",
    2424832: "left",
    2490368: "up",
    2555904: "right",
    2621440: "down"
}

img = np.zeros((200, 300), np.uint8)
cv2.namedWindow('window')
cv2.imshow('window', img)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27:
        break
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()
"""

isDragging = False
px, py = 0, 0
img = np.zeros((800, 600, 3), np.uint8)
img[:] = (255, 255, 255)
cv2.imshow("asdf", img)

def onMouseAction(event, x, y, flags, param) :
    global isDragging, px, py
    if (event == cv2.EVENT_LBUTTONDOWN) :
        print("LBD")
        isDragging = True
        px, py = x, y
    elif (event == cv2.EVENT_RBUTTONDOWN) :
        print("RBD")
        cv2.putText(img, "DUPLEX", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), 1)
    elif (event == cv2.EVENT_LBUTTONUP) :
        print("LBU")
        if (isDragging) :
            isDragging = False
            print(px, py, x, y)
            cv2.rectangle(img, (px, py), (x, y), (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), 3, cv2.LINE_4)
    elif (event == cv2.EVENT_RBUTTONUP) :
        print("RBU")
    
    cv2.imshow("asdf", img)

cv2.setMouseCallback("asdf", onMouseAction)
cv2.waitKey(0)
cv2.destroyAllWindows()