import numpy as np

arr = np.arange(1, 26).reshape(5, 5)

print("Original array:")
print(arr)

result = arr[::-1]

print("Reversed rows:")
print(result)