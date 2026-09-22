import numpy as np
arr = np.arange(1, 37).reshape(6, 6)

print("6x6 araay:")
print(arr)

corners = np.array([
    arr[0, 0],
    arr[0, -1],
    arr[-1, 0],
    arr[-1, -1]
])

print("Corner elements:", corners)