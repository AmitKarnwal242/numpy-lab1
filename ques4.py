import numpy as np
import sys

list_data = [1, 2, 3, 4, 5]
array_data = np.array([1, 2, 3, 4, 5])

print("List memory:", sys.getsizeof(list_data), "bytes")
print("NumPy array memory:", sys.getsizeof(array_data), "bytes")