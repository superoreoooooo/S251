import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# 4

print(os.getcwd())
a = cv2.imread("ImageProcessing/images_chap4/read_gray.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("a", a)
b = cv2.waitKey(0)
print(b)
cv2.destroyAllWindows()




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




img = np.full((300, 300, 3), 255, np.uint8)
cv2.line(img, (50, 50), (250, 250), (255, 0, 0), 3)
cv2.line(img, (250, 50), (50, 250), (0, 0, 255), 3)
cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




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




capture = cv2.VideoCapture(0)

while True :
    ret, frame = capture.read()
    if not ret : break
    if cv2.waitKey(30) >= 0 : break
    
    cv2.imshow("a", frame)
    
capture.release()


# 5

img = cv2.imread("test.png")
img = cv2.flip(img, -1)
#img = cv2.repeat(img, 2, 3)
img = cv2.hconcat([img, img]) #horizontal
img = cv2.vconcat([img, img]) #vertical

img = cv2.transpose(img)

cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


 #split 후 merge로 한색만뜨게하기
img = cv2.imread("ImageProcessing/images_chap5/color.jpg")
img = cv2.split(img)

print(img[0].shape)
print(np.zeros(img[0].shape, np.uint8).shape)
img = cv2.merge([np.zeros(img[0].shape, np.uint8), np.zeros(img[0].shape, np.uint8), img[2]]) 

print(img)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



img = cv2.imread("ImageProcessing/images_chap5/bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("ImageProcessing/images_chap5/logo.jpg", cv2.IMREAD_COLOR)

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1] # 임계값 이상인 픽셀만 255로 
masks = cv2.split(masks) # 채널 분리

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1]) # 0번이랑 1번채널 비교
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask) # 2번이랑 비교한 채널(0, 1번) 비교    (foreground 마스크) -> 로고 이미지 마스크
# RGB 채널 모두 비교 후 마스크 생성
bg_pass_mask = cv2.bitwise_not(fg_pass_mask) # not 연산으로 반전                         (background 마스크) -> 배경 이미지 마스크

(H, W), (h, w) = img.shape[:2], logo.shape[:2]
x, y = (W - w) // 2, (H - h) // 2
roi = img[y : y + h, x : x + w]

fg = cv2.bitwise_and(logo, logo, mask = fg_pass_mask) # 로고 이미지의 전경 (로고 부분)만 복사
bg = cv2.bitwise_and(roi, roi, mask=bg_pass_mask) # 원본 roi의 배경만 복사

dst = cv2.add(bg, fg) # 로고 전경 + 원본 배경 합성
img[y : y + h, x : x + w] = dst # 원본 이미지에 적용

cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



img1 = cv2.imread("ImageProcessing/images_chap5/abs_test1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("ImageProcessing/images_chap5/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)

difimg1 = cv2.subtract(img1, img2) # 차분
difimg2 = cv2.subtract(np.int16(img1), np.int16(img2)) # signed int 로 차분
absdif1 = np.absolute(difimg2).astype(np.uint8) # signed int -> unsigned int
absdif2 = cv2.absdiff(img1, img2) # 절대값 차분

titles = ['img1', 'img2', 'difimg1', 'absdif1', 'absdif2']
for t in titles :
    cv2.imshow(t, eval(t))
cv2.waitKey(0)



img = cv2.imread("ImageProcessing/images_chap5/minMax.jpg", cv2.IMREAD_GRAYSCALE)

min_val, max_val, _, _ = cv2.minMaxLoc(img)

ratio = 255 / (max_val - min_val)
dst = np.round((img - min_val) * ratio).astype(np.uint8)
min_val, max_val, _, _ = cv2.minMaxLoc(dst)

print(min_val, max_val)

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)



img = cv2.imread("ImageProcessing/images_chap5/sum_test.jpg", cv2.IMREAD_COLOR)

sum = cv2.sumElems(img)
mean = cv2.mean(img)
mean, stdDev = cv2.meanStdDev(img)

print(mean.flatten(), stdDev.flatten())

img = cv2.split(img)
img_b = cv2.sort(img[0], cv2.SORT_EVERY_ROW)
img_g = cv2.sort(img[1], cv2.SORT_EVERY_COLUMN)
img_r = cv2.sort(img[2], cv2.SORT_DESCENDING)

img = cv2.merge([img_b, img_g, img_r])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("A piece of modern art", img)
cv2.waitKey(0)


# 6

img1 = cv2.imread("ImageProcessing/images_chap6/add1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("ImageProcessing/images_chap6/add2.jpg", cv2.IMREAD_GRAYSCALE)

alpha, beta = 0.6, 0.7

addimg1 = cv2.add(img1, img2)
addimg2 = cv2.add(img1 * alpha, img2 * beta)
addimg2 = np.clip(addimg2, 0, 255).astype(np.uint8)
addimg3 = cv2.addWeighted(img1, alpha, img2, beta, 0)

titles = ['img1', 'img2', 'addimg1', 'addimg2', 'addimg3']
for t in titles :
    cv2.imshow(t, eval(t))
    
cv2.waitKey()




def avgFilter(img, ksize=5) :
    r, c = img.shape[:2]
    dst = np.zeros((r, c), np.uint8)
    center = ksize // 2
    
    for i in range(r) :
        for j in range(c) :
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            
            if (y1 < 0 or y2 > r or x1 < 0 or x2 > c) : dst[i, j] = img[i, j]
            else : 
                mask = img[y1 : y2, x1 : x2]
                dst[i, j] = cv2.mean(mask)[0]
    
    return dst

img = cv2.imread("ImageProcessing/images_chap6/add1.jpg", cv2.IMREAD_GRAYSCALE)

avgImg = avgFilter(img, 5)
#blurImg = cv2.blur(img, (5, 5), (-1, -1), cv2.BORDER_REFLECT) # why error ?
boxImg = cv2.boxFilter(img, ddepth=-1, ksize=(5, 5))

cv2.imshow("img", img)
cv2.imshow("avg", avgImg)
#cv2.imshow("blur", blurImg)
cv2.imshow("box", boxImg)

cv2.waitKey(0)




def onTrackbar(threshold) :
    edge = cv2.GaussianBlur(img, (5, 5), 0)
    edge = cv2.Canny(edge, threshold, threshold * 2, 5)
    
    color_edge = cv2.copyTo(img, mask=edge)
    dst = cv2.hconcat([img, color_edge])
    
    cv2.imshow("color edge", dst)
    
img = cv2.imread("ImageProcessing/images_chap7/color_edge.jpg", cv2.IMREAD_COLOR)

threshold = 50
repImg = cv2.repeat(img, 1, 2)
repGray = cv2.cvtColor(repImg, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("color edge", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Canny", "color edge", threshold, 100, onTrackbar)
onTrackbar(threshold)
cv2.waitKey(0)




img = img = cv2.imread("ImageProcessing/images_chap7/morph.jpg", cv2.IMREAD_GRAYSCALE)

#data = [0, 1, 0, 1, 1, 1, 0, 1, 0]
data = [0, 1, 0, 1, 1, 1, 0, 1, 0]

mask = np.array(data, np.uint8).reshape(3, 3)

th_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]

 #침식
dst1 = cv2.erode(th_img, mask)
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_ERODE, mask)


 #팽창
dst1 = cv2.dilate(th_img, mask)
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_DILATE, mask)


dst1 = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask)

cv2.imshow("img", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)