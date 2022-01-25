'''
Finding Expectation and Variance
'''

# Imports
import numpy as np
import matplotlib.pyplot as plt


# Main Functions
def E(P, g_x):
    '''
    Expectation
    '''
    return np.sum(P * g_x)

def Var(P, g_x):
    '''
    Variance
    '''
    E_X2 = E(P, g_x**2)
    E_X = E(P, g_x)
    return E_X2 - E_X**2

# Driver Code
# Params
def g(x):
    '''
    g(x)
    '''
    g_x = 2*x + 1
    return g_x

X = [1, 2, 3, 4, 5]
P = [0.1, 0.2, 0.3, 0.4, 0.5]
# Params

# RunCode
X = np.array(X)
P = np.array(P) / np.sum(P)

# G_X = np.array(list(map(g, X)))
G_X = g(X)

E_X = E(P, G_X)
Var_X = Var(P, G_X)

print(G_X)
print(P)
print(E_X)
print(Var_X)