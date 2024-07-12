from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some sample data
X, y = make_regression(n_samples=100, n_features=4, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply ElasticNet
elasticnet = ElasticNet(alpha=0.1, l1_ratio=0.5).fit(X_train, y_train)
y_pred = elasticnet.predict(X_test)

# Evaluate the model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
