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

# S0 = 50
# K = 50
# r = 0.1
# q = 0.05
# sigma = 0.4
# T = 0.5
# num_sim = 10000
# num_rep = 20

# SimCall = Get95ci(S0, r, q, sigma, T, K, num_sim, num_rep, 'call')
# SimPut = Get95ci(S0, r, q, sigma, T, K, num_sim, num_rep, 'put')
# print("European Call Option Value:", SimCall[0], ", 95% CI: [", SimCall[1], ", ", SimCall[2], "]")
# print("European Put Option Value:", SimPut[0], ", 95% CI: [", SimPut[1], ", ", SimPut[2], "]")