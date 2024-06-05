import pandas as pd
import numpy as np

# Basic operations
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)
print(df)
# Output:
#     Name  Age
# 0   John   28
# 1   Anna   24
# 2  Peter   35
# 3  Linda   32

# Creating Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Creating DataFrame
df = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20220101'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})
print(df)

# Selection
print(df['Name'])  # Select column

# Filtering
print(df[df['Age'] > 30])  # Filter rows
