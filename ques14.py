import numpy as np

arr1 = np.array([1, 2])
arr2 = np.array([3, 4, 5])
arr3 = np.array([6, 7, 8, 9])

arr1 = arr1.reshape(-1)
arr2 = arr2.reshape(-1)
arr3 = arr3.reshape(-1)

result = np.concatenate([arr1, arr2, arr3])

print(result)