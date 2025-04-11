import numpy as np
from scipy.stats import norm

K1 = 105
K2 = 125
K3 = 160
K4 = 200 
S0 = 100 # Current stock price
r = 0.05 # Risk-free rate
q = 0.01 # Dividend yield
sigma = 0.2 # Volatility
T = 1  # Time to maturity (yrs)

def d1(S0, K, r, sigma, T, q):
    return (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d2(S0, K, r, sigma, T, q):
    return (np.log(S0 / K) + (r - q - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def N_d(d):
    return norm.cdf(d)
