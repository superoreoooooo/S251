import cv2
import pytesseract
import numpy as np
import pyautogui
import gridSolver
import time

sizeMultiplier = 8
startX = 438
startY = 225
width, height = 0, 0

#pyautogui.mouseInfo()

def load_and_preprocessing() :
    screenshot = pyautogui.screenshot(region=(startX, startY, 1035 - startX, 601 - startY)) #?
    screenshot.save("test.png")
    img = cv2.imread('test.png')
    img = cv2.resize(img, (img.shape[1] * sizeMultiplier, img.shape[0] * sizeMultiplier))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = cv2.bitwise_or(mask1, mask2)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours, img

def ocr() :
    numbers = []
    for cnt in contours : #인식부
        x, y, w, h = cv2.boundingRect(cnt)
        #print(x, y, w, h)
        if w < 10 or h < 10:
            continue
        
        #roi = img[y:y+h, x:x+w]
        roi = img[y+2*sizeMultiplier:y+21*sizeMultiplier, x+4*sizeMultiplier:x+20*sizeMultiplier]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, gray = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
        #cv2.imwrite('test_cut.png', gray)
        
        config = "--psm 10 -c tessedit_char_whitelist=0123456789"
        text = pytesseract.image_to_string(gray, config=config)
        
        digit = text.strip()
        
        if digit.isdigit(): #7빼고 다 알아들음
            numbers.append((x, y, int(digit)))
        else :
            numbers.append((x, y, 7)) #왜 7만 인식못하니 이친구야

        width, height = w, h

    return width, height, numbers

def arrange() :
    numbers_sorted = sorted(numbers, key=lambda v : (v[1], v[0]))
    rows = []
    current_row = []
    row_tolerance = 10 #10이 최대
    appleArray = []
    posArray = [] # (x, y)

    for i, (x, y, digit) in enumerate(numbers_sorted):
        if not current_row :
            current_row.append((x, y, digit))
        else:
            _, prev_y, _ = current_row[-1]
            if abs(y - prev_y) < row_tolerance:
                current_row.append((x, y, digit))
            else:
                rows.append(current_row)
                current_row = [(x, y, digit)]

    if current_row :
        rows.append(current_row)

    for row in rows :
        row_sorted = sorted(row, key=lambda v: v[0])
        digits_in_row = [v[2] for v in row_sorted] 
        appleArray.append(digits_in_row)
        posArray.append([(v[0], v[1]) for v in row_sorted])
        
    """
    for i, row in enumerate(appleArray) :
        print(f"{row} [{len(row)}]")
    """

    return appleArray, posArray,

def drag(x, y, dx, dy) :
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(dx, dy, 0.1)
    pyautogui.mouseUp()
    time.sleep(0.1)

def execution() :
    pyautogui.moveTo(startX, startY)
    pyautogui.leftClick()
    bboxs = gridSolver.solve_grid(grid=appleArray)
    for d in bboxs :
        """
        print(d[0][1]) # -> x pos   (0, 0) : (0, 0)
        print(d[0][0]) # -> y pos   (0, 0) : (0, 0)
        print(d[1][1]) # -> dx pos  (0, 1) : (1, 0)
        print(d[1][0]) # -> dy pos  (0, 1) : (1, 0)
        """
        x, y = startX + posArray[d[0][0]][d[0][1]][0] / sizeMultiplier, startY + posArray[d[0][0]][d[0][1]][1] / sizeMultiplier
        dx, dy = startX + posArray[d[1][0]][d[1][1]][0] / sizeMultiplier, startY + posArray[d[1][0]][d[1][1]][1] / sizeMultiplier
        dx, dy = dx + width / sizeMultiplier, dy + height / sizeMultiplier
        #print(x, y, dx, dy)
        drag(x, y, dx, dy)

if __name__ == '__main__' :
    contours, img = load_and_preprocessing()
    width, height, numbers = ocr()
    appleArray, posArray = arrange()
    execution()