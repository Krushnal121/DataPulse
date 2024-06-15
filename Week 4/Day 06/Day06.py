import numpy as np
import scipy.stats as stats

# Confidence interval for a sample
data = np.random.normal(0, 1, 100)
mean = np.mean(data)
sem = stats.sem(data)
confidence_interval = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)
print("95% confidence interval:", confidence_interval)

import numpy as np
from scipy.stats import norm

# Generating sample data
data = np.random.normal(5, 2, 1000)

# MLE for mean and standard deviation
mean, std = norm.fit(data)
print("MLE Mean:", mean)
print("MLE Std Dev:", std)

import pymc as pm
import numpy as np

# Generating sample data
data = np.random.normal(0, 1, 100)

# Bayesian inference using PyMC3
with pm.Model() as model:
    mu = pm.Normal('mu', mu=0, sigma=1)
    sigma = pm.HalfNormal('sigma', sigma=1)
    observations = pm.Normal('obs', mu=mu, sigma=sigma, observed=data)
    trace = pm.sample(1000, tune=2000, return_inferencedata=False)

print(pm.summary(trace))
