import numpy as np
arr = np.array([1, 2, 3, 4, 5])
# Mathematical operations
print(np.sum(arr))  # Output: 15
print(np.mean(arr))  # Output: 3.0

# Statistical operations
print(np.std(arr))  # Output: 1.4142135623730951
print(np.var(arr))  # Output: 2.0

# Broadcasting example
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
print(arr_1 + arr_2)  # Output: [5 7 9]

# Broadcasting with scalar
scalar = 2
print(arr * scalar)  # Output: [ 2  4  6  8 10]
