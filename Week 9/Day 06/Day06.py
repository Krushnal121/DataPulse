import numpy as np
#Bagging
from sklearn.ensemble import BaggingClassifier

# Example usage
clf = BaggingClassifier()
clf.fit(X, y)
print(clf.estimators_)

# Random Subspace Method
# Custom implementation
from sklearn.tree import DecisionTreeClassifier

class RandomSubspaceMethod:
    def __init__(self, n_estimators=10, max_features='sqrt'):
        self.n_estimators = n_estimators
        self.max_features = max_features
        self.estimators = []

    def fit(self, X, y):
        for _ in range(self.n_estimators):
            clf = DecisionTreeClassifier(max_features=self.max_features)
            clf.fit(X, y)
            self.estimators.append(clf)

    def predict(self, X):
        predictions = np.array([clf.predict(X) for clf in self.estimators])
        return np.mean(predictions, axis=0)

# Example usage
clf = RandomSubspaceMethod()
clf.fit(X, y)
print(clf.predict(X))

# Random Patches Method
# Custom implementation
class RandomPatchesMethod:
    def __init__(self, n_estimators=10, max_samples=0.8, max_features=0.8):
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.max_features = max_features
        self.estimators = []

    def fit(self, X, y):
        m, n = X.shape
        for _ in range(self.n_estimators):
            sample_indices = np.random.choice(m, int(m * self.max_samples), replace=True)
            feature_indices = np.random.choice(n, int(n * self.max_features), replace=True)
            X_sample = X[sample_indices][:, feature_indices]
            y_sample = y[sample_indices]
            clf = DecisionTreeClassifier()
            clf.fit(X_sample, y_sample)
            self.estimators.append((clf, feature_indices))

    def predict(self, X):
        predictions = []
        for clf, feature_indices in self.estimators:
            predictions.append(clf.predict(X[:, feature_indices]))
        return np.mean(predictions, axis=0)

# Example usage
clf = RandomPatchesMethod()
clf.fit(X, y)
print(clf.predict(X))

# Feedforward Neural Networks
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Example usage
model = Sequential([
    Dense(10, activation='relu', input_shape=(2,)),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10)

# Convolutional Neural Networks
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D

# Example usage
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10)

# Recurrent Neural Networks
from tensorflow.keras.layers import SimpleRNN

# Example usage
model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(10, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10)

# Long Short-Term Memory Networks
from tensorflow.keras.layers import LSTM

# Example usage
model = Sequential([
    LSTM(50, activation='relu', input_shape=(10, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10)
