import numpy as np


A = np.array([[1, 2, 1], [1, 1, 1], [2, 4, 3]])
AInv = np.linalg.inv(A)

print(AInv)

print(A.dot(AInv))