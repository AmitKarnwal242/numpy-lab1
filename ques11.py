import numpy as np

arr = np.random.randint(1, 100, 10)

max_value = np.max(arr)
max_index = np.argmax(arr)

print("Array:", arr)
print("Maximum value:", max_value)
print("Index:", max_index)