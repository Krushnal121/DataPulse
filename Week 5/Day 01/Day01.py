import pandas as pd

# Load dataset
data = pd.read_csv('data.csv')

# Descriptive statistics
print(data.describe())

from scipy import stats

# Hypothesis testing
t_stat, p_value = stats.ttest_ind(data['group1'], data['group2'])
print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Correlation matrix
correlation_matrix = data.corr()
print(correlation_matrix)

import statsmodels.api as sm

# Regression analysis
X = data[['feature1', 'feature2']]
y = data['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
