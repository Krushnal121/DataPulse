import numpy as np
# Adadelta
def adadelta(X, y, epochs=1000, rho=0.95, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    Eg = np.zeros(n)
    Edx = np.zeros(n)
    delta_theta = np.zeros(n)
    for epoch in range(epochs):
        gradients = 2/m * X.T.dot(X.dot(theta) - y)
        Eg = rho * Eg + (1 - rho) * gradients**2
        rms_g = np.sqrt(Eg + epsilon)
        rms_dx = np.sqrt(Edx + epsilon)
        delta_theta = -rms_dx / rms_g * gradients
        Edx = rho * Edx + (1 - rho) * delta_theta**2
        theta += delta_theta
    return theta

# Example usage
theta = adadelta(X, y)
print(theta)

# RMSprop

def rmsprop(X, y, learning_rate=0.01, epochs=1000, beta=0.9, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    Eg = np.zeros(n)
    for epoch in range(epochs):
        gradients = 2/m * X.T.dot(X.dot(theta) - y)
        Eg = beta * Eg + (1 - beta) * gradients**2
        adjusted_gradients = gradients / (np.sqrt(Eg) + epsilon)
        theta -= learning_rate * adjusted_gradients
    return theta

# Example usage
theta = rmsprop(X, y)
print(theta)

#Adam

def adam(X, y, learning_rate=0.01, epochs=1000, beta1=0.9, beta2=0.999, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    m_t = np.zeros(n)
    v_t = np.zeros(n)
    for epoch in range(1, epochs + 1):
        gradients = 2/m * X.T.dot(X.dot(theta) - y)
        m_t = beta1 * m_t + (1 - beta1) * gradients
        v_t = beta2 * v_t + (1 - beta2) * gradients**2
        m_hat = m_t / (1 - beta1**epoch)
        v_hat = v_t / (1 - beta2**epoch)
        theta -= learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
    return theta

# Example usage
theta = adam(X, y)
print(theta)
