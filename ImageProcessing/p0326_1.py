import cv2
import numpy as np

data = np.random.randint(0, 256, 15, np.uint8).tolist()

print(data)

m1 = np.reshape(data, (3, 5))
m2 = np.full((3, 5), 50)

m_min = cv2.min(m1, 30)
m_max = cv2.max(m1, m2)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(m1)

print(f"m1 = \n{m1}\n")
print(f"m_min = \n{m_min}\n")
print(f"m_max = \n{m_max}\n")

print(f"min_val = {min_val}, min_loc = {min_loc}")
print(f"max_val = {max_val}, max_loc = {max_loc}")