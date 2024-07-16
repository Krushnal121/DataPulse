#Momentum
import numpy as np
def gradient_descent_with_momentum(X, y, learning_rate=0.01, epochs=1000, momentum=0.9):
    m, n = X.shape
    theta = np.zeros(n)
    v = np.zeros(n)
    for epoch in range(epochs):
        gradients = 2/m * X.T.dot(X.dot(theta) - y)
        v = momentum * v - learning_rate * gradients
        theta += v
    return theta

# Example usage
theta = gradient_descent_with_momentum(X, y)
print(theta)

#Nesterov Accelerated Gradient Descent
def nesterov_accelerated_gradient_descent(X, y, learning_rate=0.01, epochs=1000, momentum=0.9):
    m, n = X.shape
    theta = np.zeros(n)
    v = np.zeros(n)
    for epoch in range(epochs):
        look_ahead = theta + momentum * v
        gradients = 2/m * X.T.dot(X.dot(look_ahead) - y)
        v = momentum * v - learning_rate * gradients
        theta += v
    return theta

# Example usage
theta = nesterov_accelerated_gradient_descent(X, y)
print(theta)

#Adagrad
def adagrad(X, y, learning_rate=0.01, epochs=1000, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    G = np.zeros(n)
    for epoch in range(epochs):
        gradients = 2/m * X.T.dot(X.dot(theta) - y)
        G += gradients**2
        adjusted_gradients = gradients / (np.sqrt(G) + epsilon)
        theta -= learning_rate * adjusted_gradients
    return theta

# Example usage
theta = adagrad(X, y)
print(theta)
