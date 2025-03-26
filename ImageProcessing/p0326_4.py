import cv2
import numpy as np

cnt = 0

while True :
    if cv2.waitKey(30) >= 0 :
        break
    theta = cnt * 10 * np.pi / 180
    cnt += 1
    rotMat = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]], np.float32)

    pts1 = np.array([(250, 30), (400, 70), (350, 250), (150, 200)], np.float32)
    pts2 = cv2.gemm(pts1, rotMat, 1, None, 1, flags=cv2.GEMM_2_T)

    for i, (pt1, pt2) in enumerate(zip(pts1, pts2)) :
        print(f"i={i}, pt1={pt1}, pt2={pt2}")

    img = np.full((400, 500, 3), 255, np.uint8)
    cv2.polylines(img, [np.int32(pts1)], True, (0, 255, 0), 2)
    cv2.polylines(img, [np.int32(pts2)], True, (255, 0, 0), 3)

    cv2.imshow('img', img)
    

cv2.destroyAllWindows()