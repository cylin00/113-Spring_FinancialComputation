import numpy as np
from scipy.stats import norm

def d1(S0, K, r, sigma, T, q):
    return (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d2(S0, K, r, sigma, T, q):
    return (np.log(S0 / K) + (r - q - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def N_d(d):
    return norm.cdf(d)

def option_price(S0, r, q, sigma, T, K1, K2, K3, K4):
    sec1 = S0 * np.exp(-q * T) * (N_d(d1(S0, K1, r, sigma, T, q)) - N_d(d1(S0, K2, r, sigma, T, q))) - K1 * np.exp(-r * T) * (N_d(d2(S0, K1, r, sigma, T, q)) - N_d(d2(S0, K2, r, sigma, T, q)))
    sec2 = np.exp(-r * T) * (K2 - K1) * (N_d(d2(S0, K2, r, sigma, T, q)) - N_d(d2(S0, K3, r, sigma, T, q)))
    sec3 = ((K2 - K1)/(K4 - K3)) * (np.exp(-r * T) * K4 * (N_d(d2(S0, K3, r, sigma, T, q)) - N_d(d2(S0, K4, r, sigma, T, q))) - S0 * np.exp(-q * T) * (N_d(d1(S0, K3, r, sigma, T, q)) - N_d(d1(S0, K4, r, sigma, T, q))))
    return sec1 + sec2 + sec3