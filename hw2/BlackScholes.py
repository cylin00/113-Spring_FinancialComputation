import numpy as np
from scipy.stats import norm

def d1(S0, K, r, sigma, T, q):
    return (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d2(S0, K, r, sigma, T, q):
    return (np.log(S0 / K) + (r - q - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def N(d):
    return norm.cdf(d)

def GetOptionValue(S0, K, r, q, sigma, T, option_type = 'call'):
    if option_type == 'call':
        return S0 * np.exp(-q * T) * N(d1(S0, K, r, sigma, T, q)) - K * np.exp(-r * T) * N(d2(S0, K, r, sigma, T, q))
    else:
        return K * np.exp(-r * T) * N(-d2(S0, K, r, sigma, T, q)) - S0 * np.exp(-q * T) * N(-d1(S0, K, r, sigma, T, q))