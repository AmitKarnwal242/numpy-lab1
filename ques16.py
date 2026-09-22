import numpy as np

arr = np.arange(32).reshape(2, 4, 4)

result = np.split(arr, 2, axis=0)

print("Original array:")
print(arr)

print("\nPart 1:")
print(result[0])

print("\nPart 2:")
print(result[1])