import numpy as np

def Get95ci(S0, r, q, sigma, T, K, n_sim, n_rep, option_type = 'call'):

    prices = []

    for i in range(n_rep):
        
        mean = np.log(S0) + (r - q - 0.5 * sigma **2) * T
        std = sigma * np.sqrt(T)
        lnST = np.random.normal(mean, std, n_sim)
        ST = np.exp(lnST)

        if option_type == 'call':
            payoff = np.maximum(ST - K, 0)  
        else:
            payoff = np.maximum(K - ST, 0)  

        price = np.exp(-r * T) * np.mean(payoff)
        prices.append(price)

    mean_price = np.mean(prices)
    std_price = np.std(prices)
    ci_low = mean_price - 2 * std_price
    ci_high = mean_price + 2 * std_price

    return mean_price, ci_low, ci_high