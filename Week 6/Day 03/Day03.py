from sklearn.manifold import TSNE

# Assuming X from previous snippets
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)
print(X_tsne)


from keras.layers import Input, Dense
from keras.models import Model
import numpy as np

# Sample data
X = np.array([[0., 1.], [1., 0.], [0., 0.], [1., 1.]])

input_dim = X.shape[1]
encoding_dim = 2

input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='sigmoid')(encoded)

autoencoder = Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder.fit(X, X, epochs=50, batch_size=2, shuffle=True)


from sklearn.model_selection import train_test_split

# Assuming X and y from previous snippets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train, X_test, y_train, y_test)
