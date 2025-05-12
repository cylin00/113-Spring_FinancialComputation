import numpy as np
import math

def GetOptionValue(K, r, T, n_sim, n_rep, n, S0, q, sigma, corr):

    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            C[i, j] = sigma[i] * sigma[j] * corr[i, j] * T
    A = Decomposition(C)

    option_val = []
    for i in range(n_rep):

        z = np.zeros((n_sim, n))
        for j in range(n):
            z[:, j] = np.random.normal(0, 1, n_sim)
        r_t = np.matmul(z, A)

        payoff = np.zeros((n_sim, 1))
        ST = np.zeros(r_t.shape)
        ST_max = np.zeros((n_sim, 1))
        for i in range(n_sim):
            ST_m, j_m = 0, 0
            for j in range(n):
                ST[i, j] = np.exp(r_t[i, j] + np.log(S0[j]) + (r - q[j] - 0.5 * sigma[j] ** 2) * T)
                if ST[i, j] > ST_m:
                    ST_m = ST[i, j]
                    j_m = j
            ST_max[i] = np.max(ST[i, :])
            payoff[i] = np.maximum(ST_max[i] - K, 0)

        option_val.append(np.exp(-r * T) * np.mean(payoff))

    option_value = np.mean(option_val)
    option_std = np.std(option_val)
    ci_low = option_value - 2 * option_std
    ci_high = option_value + 2 * option_std
    return option_value, ci_low, ci_high

def Decomposition(cov):
    A = np.zeros(cov.shape)
    A[0, 0] = np.sqrt(cov[0, 0])  # A[1, 1]

    for j in range(1, cov.shape[0]): # A[1, 2], A[1, 3], ...
        A[0, j] = cov[0, j] / A[0, 0]

    for i in range(1, cov.shape[0]-1): # next rows
        temp_sum = 0
        for k in range(i):
            temp_sum += A[k, i] ** 2
        A[i, i] = math.sqrt(cov[i, i] - temp_sum)

        for j in range(i + 1, cov.shape[0]):
            temp_sum = 0
            for k in range(i):
                temp_sum += A[k, i] * A[k, j]
            A[i, j] = (cov[i, j] - temp_sum) / A[i, i]
        
    temp_sum = 0
    for k in range(cov.shape[0]-1):
        temp_sum += A[k, cov.shape[0]-1] ** 2
    A[cov.shape[0]-1, cov.shape[0]-1] = math.sqrt(cov[cov.shape[0]-1, cov.shape[0]-1] - temp_sum)

    return A
