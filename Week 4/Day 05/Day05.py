# Bayes' theorem calculation
P_A = 0.3
P_B_given_A = 0.8
P_B = 0.5

P_A_given_B = (P_B_given_A * P_A) / P_B
print("P(A|B):", P_A_given_B)

import numpy as np
import matplotlib.pyplot as plt

# Simulating CLT with random samples
sample_means = []
for _ in range(1000):
    sample = np.random.randn(100)
    sample_means.append(np.mean(sample))

plt.hist(sample_means, bins=30)
plt.title('Central Limit Theorem')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()

from scipy import stats

# Example t-test
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(0.5, 1, 100)

t_stat, p_val = stats.ttest_ind(data1, data2)
print("T-statistic:", t_stat)
print("P-value:", p_val)
