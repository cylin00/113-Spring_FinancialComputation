import numpy as np

def get_payoff(ST, K1, K2, K3, K4):

    payoff = np.piecewise(
        ST,
        [ST < K1, (K1 <= ST) & (ST < K2), (K2 <= ST) & (ST < K3), (K3 <= ST) & (ST <= K4), ST > K4],
        [0, lambda s : s - K1, lambda s : K2 - K1, lambda s : (K2 - K1) * (K4 - s) / (K4 - K3), 0]
    )

    return payoff

def get_95ci(S0, r, q, sigma, T, K1, K2, K3, K4):

    prices = []

    for i in range(20):
        
        mean = np.log(S0) + (r - q - 0.5 * sigma **2) * T
        std = sigma * np.sqrt(T)
        lnST = np.random.normal(mean, std, 10000)
        ST = np.exp(lnST)

        payoff = get_payoff(ST, K1, K2, K3, K4)
        price = np.exp(-r * T) * np.mean(payoff)
        prices.append(price)

    mean_price = np.mean(prices)
    std_price = np.std(prices)
    ci_low = mean_price - 2 * std_price
    ci_high = mean_price + 2 * std_price

    return mean_price, ci_low, ci_high