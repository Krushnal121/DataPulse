from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# Assuming X and y from previous snippets
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=5)
print(scores)

from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1, 1, 10], 'solver': ['lbfgs', 'liblinear']}
grid = GridSearchCV(LogisticRegression(), param_grid, refit=True, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_)

