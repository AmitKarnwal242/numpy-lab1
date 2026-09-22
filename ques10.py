import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

transpose = np.transpose(arr)

print("Original matrix:")
print(arr)

print("Transpose:")
print(transpose)

print("Transpose of transpose:")
print(np.transpose(transpose))

print("Same as original:", np.array_equal(arr, np.transpose(transpose)))