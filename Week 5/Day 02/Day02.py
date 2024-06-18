import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
import pandas as pd

# ANOVA
anova_model = ols('target ~ C(group)', data=data).fit()
anova_table = sm.stats.anova_lm(anova_model, typ=2)
print(anova_table)

# Mann-Whitney U Test
u_stat, p_value = stats.mannwhitneyu(data['group1'], data['group2'])
print(f"U-statistic: {u_stat}, P-value: {p_value}")

import matplotlib.pyplot as plt

# Time series plot
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
data['value'].plot()
plt.show()

import random

# Randomly assign subjects to groups
subjects = list(data['subject'])
random.shuffle(subjects)
group1 = subjects[:len(subjects)//2]
group2 = subjects[len(subjects)//2:]
print(f"Group 1: {group1}, Group 2: {group2}")
