import numpy as np

arr = np.arange(1, 18)

parts = np.array_split(arr, 4)

for i, part in enumerate(parts):
    print("Part", i + 1, ":", part)
    print("Size:", len(part))