import cv2
import numpy as np

"""
t1 = cv2.imread("ImageProcessing/images_chap4/read_color.jpg", cv2.IMREAD_GRAYSCALE)
t2 = cv2.imread("ImageProcessing/images_chap4/read_color.jpg", cv2.IMREAD_COLOR)

print(f"{t1.shape}, {t2.shape}")
print(f"{t1[100, 100]}, {t2[100, 100]}")

cv2.imshow("t1", t1)
cv2.imshow("t2", t2)

cv2.imwrite("ImageProcessing/images_chap4/write_bmp.bmp", t2)

cv2.waitKey(0)
cv2.destroyAllWindows()"
"""

def put_string(frame, text, pt, value, color=(120, 200, 90)) :
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)

def zoom_bar(value) :   
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value)

def focus_bar(value) :
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)

capture = cv2.VideoCapture(0)
if (capture.isOpened() == False) :
    print("Camera is not opened")
    exit()

capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)

fps = 29.97
delay = round(1000/fps)
size = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')

writer = cv2.VideoWriter("ImageProcessing/images_chap4/write_video.avi", fourcc, fps, size)
if (writer.isOpened == False) : raise Exception("?")

title = "Camera"
cv2.namedWindow(title)
"""
cv2.createTrackbar('zoom', title, 0, 10, zoom_bar)
cv2.createTrackbar('focus', title, 0, 40, focus_bar)
"""

print("Frame width: ", int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Frame height: ", int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Frame rate: ", int(capture.get(cv2.CAP_PROP_FPS)))

while True :
    ret, frame = capture.read()
    if not ret :
        break
    if cv2.waitKey(30) >= 0 :
        break

    """
    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, "Exposure: ", (10, 40), exposure)
    put_string(frame, "Frame: ", (10, 80), int(capture.get(cv2.CAP_PROP_FPS)))

    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))
    put_string(frame, "Zoom: ", (10, 240), zoom)
    put_string(frame, "Focus: ", (10, 280), focus)
    """
    logo = cv2.imread('ImageProcessing/images_chap5/logo.jpg', cv2.IMREAD_COLOR)

    masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
    masks = cv2.split(masks)

    fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
    fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
    bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

    (H, W), (h, w) = frame.shape[:2], logo.shape[:2]
    x, y = (W-w)//2, (H-h)//2   
    roi = frame[y:y+h, x:x+w]

    fg = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
    bg = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

    dst = cv2.add(bg, fg)
    frame[y:y+h, x:x+w] = dst

    writer.write(frame)
    cv2.imshow(title, frame)

writer.release()
capture.release()
cv2.destroyAllWindows()