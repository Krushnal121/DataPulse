from sklearn.model_selection import train_test_split

# Sampling
train, test = train_test_split(data, test_size=0.2, random_state=42)
print(f"Train shape: {train.shape}, Test shape: {test.shape}")
