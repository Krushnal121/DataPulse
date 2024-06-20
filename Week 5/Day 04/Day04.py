# Log transformation
data['log_value'] = data['value'].apply(np.log)

from sklearn.preprocessing import MinMaxScaler

# Normalization
scaler = MinMaxScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])
print(data.head())

from sklearn.preprocessing import StandardScaler

# Scaling
scaler = StandardScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])
print(data.head())

import pandas as pd
# One-hot encoding
data = pd.get_dummies(data, columns=['categorical_feature'], drop_first=True)
print(data.head())
