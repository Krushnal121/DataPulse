import statsmodels.api as sm

# Logistic regression
X = data[['feature1', 'feature2']]
y = data['target']
X = sm.add_constant(X)
logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())

from scipy import stats

# Confidence intervals
mean, sigma = data['value'].mean(), data['value'].std()
ci = stats.norm.interval(0.95, loc=mean, scale=sigma)
print(f"95% confidence interval: {ci}")

import pymc3 as pm

# Bayesian inference
with pm.Model() as model:
    mu = pm.Normal('mu', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=10)
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=data['value'])
    trace = pm.sample(1000)
pm.traceplot(trace)

# Fill missing values
data.fillna(data.mean(), inplace=True)
print(data.isnull().sum())

