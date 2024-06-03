import numpy as np

# Basic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Output: [5 7 9]


# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

# Multi-dimensional array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]


# Indexing
print(arr[0])  # Output: 1

# Slicing
print(arr[1:4])  # Output: [2 3 4]
print(arr_2d[0, 1])  # Output: 2
print(arr_2d[:, 1])  # Output: [2 5]
