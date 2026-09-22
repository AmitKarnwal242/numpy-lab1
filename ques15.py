import numpy as np

arr = np.arange(1, 17)

matrix = arr.reshape(4, 4)

result = np.transpose(matrix)

print("Original matrix:")
print(matrix)

print("Transpose:")
print(result)