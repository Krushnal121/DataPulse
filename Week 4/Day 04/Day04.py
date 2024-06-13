import numpy as np
# SVD of a matrix
matrix = np.array([[1, 2], [3, 4]])
U, S, V = np.linalg.svd(matrix)
print("U matrix:\n", U)
print("Singular values:", S)
print("V matrix:\n", V)

import scipy.stats as stats

# Normal distribution
mean = 0
std_dev = 1
distribution = stats.norm(mean, std_dev)
print("Probability density at x=0:", distribution.pdf(0))

# Example of conditional probability using Bayes' theorem
P_A = 0.3
P_B_given_A = 0.8
P_B = 0.5

P_A_given_B = (P_B_given_A * P_A) / P_B
print("P(A|B):", P_A_given_B)
