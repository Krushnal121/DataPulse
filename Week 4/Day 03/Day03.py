import numpy as np

# Transpose of a matrix
matrix = np.array([[1, 2], [3, 4]])
transpose = np.transpose(matrix)
print("Transpose:\n", transpose)

# Determinant of a matrix
matrix = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(matrix)
print("Determinant:", determinant)

# Eigenvalues and eigenvectors
matrix = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
