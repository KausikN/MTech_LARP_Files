'''
Distributions Calculator
'''

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, expon, beta, gamma, lognorm
import scipy.stats as stats

# Main Functions
def PlotDistribution_Continuous(dist, X, title, x_label, y_label):
    '''
    Plot a distribution
    '''
    x = X
    y = dist.pdf(x)
    plt.plot(x, y, label=title)
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Driver Code
# Params
Dist = norm(loc=0, scale=1)
# Dist = uniform(loc=0, scale=1)
# Dist = expon(scale=1)
# Dist = beta(a=1, b=1)
# Dist = gamma(a=1, scale=1)
# Dist = lognorm(s=1, scale=1)
# Params

# RunCode
X = np.linspace(-1.0, 1.0, 100)
PlotDistribution_Continuous(Dist, X, 'Distribution', 'X', 'Y')
# Y = Dist.pdf(X)
# print(Y)