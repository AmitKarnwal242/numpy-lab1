import numpy as np

marks = np.array([
    [80, 75, 90, 85],
    [70, 80, 75, 85],
    [90, 85, 95, 80],
    [60, 70, 65, 75],
    [85, 90, 80, 95]
])

student_average = np.mean(marks, axis=1)
subject_average = np.mean(marks, axis=0)

print("Student averages:")
print(student_average)

print("Subject averages:")
print(subject_average)