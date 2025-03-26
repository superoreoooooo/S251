import cv2
import numpy as np

m1 = np.full((3, 6), 10, np.uint8)
m2 = np.full((3, 6), 50, np.uint8)

m_mask = np.zeros(m1.shape, np.uint8)
m_mask[:, 3:] = 1

m_add1 = cv2.add(m1, m2)
m_add2 = cv2.add(m1, m2, mask=m_mask)

m_div1 = cv2.divide(m1, m2)
m1 = m1.astype(np.float32)
m2 = np.float32(m2)
m_div2 = cv2.divide(m1, m2)

titles = ['m1', 'm2', 'm_mask', 'm_add1', 'm_add2', 'm_div1', 'm_div2']

for t in titles:
    print(f"{t} = \n{eval(t)}\n")