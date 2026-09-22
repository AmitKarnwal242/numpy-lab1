import numpy as np

arr = np.array([10, 12, 11, 13, 12, 100, 11, 10])

mean = np.mean(arr)
std = np.std(arr)

lower = mean - 2 * std
upper = mean + 2 * std

outliers = arr[(arr < lower) | (arr > upper)]
cleaned = arr[(arr >= lower) & (arr <= upper)]

print("Mean:", mean)
print("Standard deviation:", std)
print("Outliers:", outliers)
print("Array after removing outliers:", cleaned)