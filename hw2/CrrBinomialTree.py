import numpy as np
import math

def GetEuropeanOptionValue(S0, K, r, q, sigma, T, n, option_type = 'call'):
    u = np.exp(sigma * np.sqrt(T / n))
    d = np.exp(-sigma * np.sqrt(T / n))
    p = (np.exp((r - q) * T / n) - d) / (u - d)

    stock_tree = np.full((n+1, n+1), np.nan)
    option_tree = np.full((n+1, n+1), np.nan)
    for i in range(n+1):
        for j in range(i+1):
            stock_tree[j, i] = S0 * u**(i-j) * d**j

    if option_type == 'call':
        option_tree[:n+1, n] = np.maximum(stock_tree[:n+1, n] - K, 0)
    else:
        option_tree[:n+1, n] = np.maximum(K - stock_tree[:n+1, n], 0)

    for i in reversed(range(n)):
        for j in range(i+1):
            option_tree[j, i] = np.exp(-r * T / n) * (p * option_tree[j, i+1] + (1 - p) * option_tree[j+1, i+1])

    return option_tree[0, 0]

def GetAmericanOptionValue(S0, K, r, q, sigma, T, n, option_type = 'call'):
    u = np.exp(sigma * np.sqrt(T / n))
    d = np.exp(-sigma * np.sqrt(T / n))
    p = (np.exp((r - q) * T / n) - d) / (u - d)

    stock_tree = np.full((n+1, n+1), np.nan)
    option_tree = np.full((n+1, n+1), np.nan)
    for i in range(n+1):
        for j in range(i+1):
            stock_tree[j, i] = S0 * u**(i-j) * d**j

    if option_type == 'call':
        option_tree[:n+1, n] = np.maximum(stock_tree[:n+1, n] - K, 0)
    else:
        option_tree[:n+1, n] = np.maximum(K - stock_tree[:n+1, n], 0)

    for i in reversed(range(n)):
        for j in range(i+1):
            hold = np.exp(-r * T / n) * (p * option_tree[j, i+1] + (1 - p) * option_tree[j+1, i+1])

            if option_type == 'call':
                exercise = stock_tree[j, i] - K
            else:
                exercise = K - stock_tree[j, i]

            option_tree[j, i] = max(hold, exercise)

    return option_tree[0, 0]

def GetEuropean_1D(S0, K, r, q, sigma, T, n, option_type = 'call'):
    u = np.exp(sigma * np.sqrt(T / n))
    d = np.exp(-sigma * np.sqrt(T / n))
    p = (np.exp((r - q) * T / n) - d) / (u - d)

    prices = np.array([S0 * u**(n - i) * d**i for i in range(n + 1)])
    if option_type == 'call':
        values = np.maximum(prices - K, 0)
    else:
        values = np.maximum(K - prices, 0)

    for i in reversed(range(n)):
        values = np.exp(-r * T / n) * (p * values[:-1] + (1 - p) * values[1:])

    return values[0]

def GetAmerican_1D(S0, K, r, q, sigma, T, n, option_type = 'call'):
    u = np.exp(sigma * np.sqrt(T / n))
    d = np.exp(-sigma * np.sqrt(T / n))
    p = (np.exp((r - q) * T / n) - d) / (u - d)

    prices = np.array([S0 * (u**(n - i)) * (d**i) for i in range(n + 1)])
    if option_type == 'call':
        values = np.maximum(prices - K, 0)
    else:
        values = np.maximum(K - prices, 0)

    for i in reversed(range(n)):
        for j in range(i+1):
            stock_price = S0 * (u ** (i - j)) * (d ** j)  
            hold = np.exp(-r * T / n) * (p * values[j] + (1-p) * values[j+1])
            if option_type == 'call':
                exercise = stock_price - K
            else:
                exercise = K - stock_price
            values[j] = max(hold, exercise)

    return values[0]

def GetEuropean_Combinatorial(S0, K, r, q, sigma, T, n, option_type = 'call'):
    u = np.exp(sigma * np.sqrt(T / n))
    d = np.exp(-sigma * np.sqrt(T / n))
    p = (np.exp((r - q) * T / n) - d) / (u - d)

    option_T = 0
    if option_type == 'call':
        for j in range(n+1):
            option_T += np.exp(math.log(math.factorial(n)) - math.log(math.factorial(j)) - math.log(math.factorial(n-j)) + (n-j)*math.log(p) + j*math.log(1-p) ) * np.maximum(S0 * u**(n-j) * d**j - K, 0)
    else:
        for j in range(n+1):
            option_T += np.exp(math.log(math.factorial(n)) - math.log(math.factorial(j)) - math.log(math.factorial(n-j)) + (n-j)*math.log(p) + j*math.log(1-p) ) * np.maximum(K - S0 * u**(n-j) * d**j, 0)
    
    option_value = np.exp(-r * T) * option_T

    return option_value