import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25])

# Create linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('Simple Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data
data = {'X1': [1, 2, 3, 4, 5], 'X2': [2, 4, 6, 8, 10], 'y': [1, 3, 5, 7, 9]}
df = pd.DataFrame(data)

X = df[['X1', 'X2']]
y = df['y']

# Create linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)
print("Predicted values:", y_pred)
