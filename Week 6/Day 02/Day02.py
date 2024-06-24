from sklearn.decomposition import PCA

# Assuming X from previous snippets
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(X_reduced)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Assuming X and y from previous snippets
lda = LinearDiscriminantAnalysis(n_components=1)
X_lda = lda.fit_transform(X, y)
print(X_lda)

