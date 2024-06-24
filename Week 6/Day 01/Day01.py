from sklearn.feature_selection import SelectKBest, chi2
import pandas as pd

# Sample data
data = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [2, 3, 4, 5, 6],
    'feature3': [5, 4, 3, 2, 1],
    'label': [1, 0, 1, 0, 1]
})

X = data[['feature1', 'feature2', 'feature3']]
y = data['label']

# Select the best 2 features
selector = SelectKBest(score_func=chi2, k=2)
X_new = selector.fit_transform(X, y)
print(X_new)

from sklearn.decomposition import PCA

# Assuming X from previous snippet
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(X_pca)

from sklearn.preprocessing import OneHotEncoder

# Sample data
data = pd.DataFrame({
    'color': ['red', 'green', 'blue', 'green', 'red']
})

encoder = OneHotEncoder(sparse=False)
encoded_data = encoder.fit_transform(data)
print(encoded_data)
