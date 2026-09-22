import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Before:", arr)
print("Before dtype:", arr.dtype)

arr = arr.astype(float)

print("After:", arr)
print("After dtype:", arr.dtype)