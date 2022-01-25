'''
Distributions Calculator
'''

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, geom, hypergeom, nbinom, poisson
import scipy.stats as stats

# Main Functions
def PlotDistribution_Discrete(dist, X, title, x_label, y_label):
    '''
    Plot a distribution
    '''
    x = X
    y = dist.pmf(x)
    plt.plot(x, y, label=title)
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Driver Code
# Params
# Dist = binom(n=8, p=0.4)
# Dist = geom(p=0.25)
# Dist = hypergeom(n=100, M=50, N=25)
# Dist = nbinom(n=100, p=0.25)
Dist = poisson(mu=8)
# Params

# RunCode
# X = np.arange(0, 101)
# X = np.array([])
# PlotDistribution_Discrete(Dist, X, 'Distribution', 'X', 'Y')
X = np.array([8])
Y = Dist.pmf(X)
print(Y)
# print(32*np.exp(-4)/3)
# print(np.exp(1))