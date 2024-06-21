from sklearn.impute import SimpleImputer

# Imputation
imputer = SimpleImputer(strategy='mean')
data[['feature1']] = imputer.fit_transform(data[['feature1']])
print(data.isnull().sum())

# Dropping rows with missing data
data.dropna(inplace=True)
print(data.isnull().sum())

from sklearn.decomposition import PCA

# PCA for dimensionality reduction
pca = PCA(n_components=2)
data_reduced = pca.fit_transform(data[['feature1', 'feature2', 'feature3']])
print(data_reduced)

import pandas as pd
# Merge datasets
data2 = pd.read_csv('data2.csv')
merged_data = pd.merge(data, data2, on='common_feature')
print(merged_data.head())
