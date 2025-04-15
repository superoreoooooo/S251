import numpy as np

print(np.linspace(0, 10, 21))
print(np.arange(0, 10, 1, dtype=np.float32))

a = np.random.randint(0, 10, (3, 4))
b = np.random.randint(0, 10, (3, 4))

print(a, b)

print(a - b)


#86p