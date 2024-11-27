import numpy as np

# The Discrete Gradient Linear Operator
# grad: R^{256x256} -> R^{2x256x256}
def grad(X):
    G = np.zeros_like([X, X])
    G[0, :, :-1] = X[:, 1:] - X[:, :-1] # Horizontal Direction
    G[1, :-1, :] = X[1:, :] - X[:-1, :] # Vertical Direction
    return G

# The Adjoint of the Discrete Gradient Linear Operator
# grad_T: R^{2x256x256} -> R^{256x256}
def grad_T(Y):
    G_T = np.zeros_like(Y[0])

    G_T[:, :-1] += Y[0, :, :-1] # Corresponds to c[0]
    G_T[:-1, :] += Y[1, :-1, :] # Corresponds to c[1]
    G_T[:, 1:] -= Y[0, :, :-1] # Corresponds to c[0]
    G_T[1:, :] -= Y[1, :-1, :] # Corresponds to c[1]

    return G_T
