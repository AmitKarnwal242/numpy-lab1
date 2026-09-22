import numpy as np
arr = np.array([1, 3, 5, 6, 8, 9, 10, 12, 15])
print("before replace array:",arr)

#for replacing every element divisible by 3 in array with -1
arr[arr % 3 == 0] = -1

print("after replace array:",arr)