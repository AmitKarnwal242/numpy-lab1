import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([15, 25, 35, 45, 55])

result = np.corrcoef(arr1, arr2)

print(result)