from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

param_dist = {'C': uniform(0.1, 10)}
random_search = RandomizedSearchCV(LogisticRegression(), param_distributions=param_dist, n_iter=100, cv=5)
random_search.fit(X_train, y_train)
print(random_search.best_params_)

from sklearn.metrics import confusion_matrix

# Assuming y_test from previous snippets and some predictions
y_pred = grid.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
