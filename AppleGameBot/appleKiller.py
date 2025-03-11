import cv2
import pytesseract
import numpy as np

"""

screenshot = pyautogui.screenshot(region=(438, 225, 1065 - 468, 601 - 225))
screenshot.save("test.png")
img = np.array(screenshot)

"""
sizeMultiplier = 8

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

numbers = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w < 10 or h < 10:
        continue
    
    #roi = img[y:y+h, x:x+w]
    roi = img[y+2*sizeMultiplier:y+21*sizeMultiplier, x+4*sizeMultiplier:x+20*sizeMultiplier]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite('test_cut.png', gray)
    
    config = "--psm 10 -c tessedit_char_whitelist=0123456789"
    text = pytesseract.image_to_string(gray, config=config)
    
    digit = text.strip()
    
    if digit.isdigit():
        numbers.append((x, y, digit))
    else :
        numbers.append((x, y, '7')) #왜 7만 인식못하니 이친구야

numbers_sorted = sorted(numbers, key=lambda v: (v[1], v[0]))
rows = []
current_row = []
row_tolerance = 15 
for i, (x, y, digit) in enumerate(numbers_sorted):
    if not current_row:
        current_row.append((x, y, digit))
    else:
        _, prev_y, _ = current_row[-1]
        if abs(y - prev_y) < row_tolerance:
            current_row.append((x, y, digit))
        else:
            rows.append(current_row)
            current_row = [(x, y, digit)]

if current_row:
    rows.append(current_row)

two_d_array = []
for row in rows:
    row_sorted = sorted(row, key=lambda v: v[0])
    digits_in_row = [v[2] for v in row_sorted] 
    two_d_array.append(digits_in_row)

for i, row in enumerate(two_d_array):
    print(f"Row {i}: {row} [{len(row)}]")