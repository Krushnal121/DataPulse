import pandas as pd
import numpy as np

# Handling missing data
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [np.nan, 2, 3]})
print(df.dropna())  # Drop rows with missing data
print(df.fillna(0))  # Fill missing data with 0

# Sorting
print(df.sort_values(by='A'))

# Aggregation
print(df.groupby('B').sum())
