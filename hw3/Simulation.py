import numpy as np
import CholeskyDecomposition as cd

def GetOptionValue(K, r, T, n_sim, n_rep, n, S0, q, sigma, corr):

    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            C[i, j] = sigma[i] * sigma[j] * corr[i, j] * T
    A = cd.Decomposition(C)
    
    option_val = []
    option_val_bonus1 = []
    option_val_bonus2 = []
    for rep in range(n_rep):

        z = np.zeros((n_sim, n))
        for j in range(n):
            z[:, j] = np.random.normal(0, 1, n_sim)
        r_t = np.matmul(z, A)
        payoff = np.zeros((n_sim, 1))
        ST = np.zeros(r_t.shape)

        # Basic requirement
        for i in range(n_sim):
            for j in range(n):
                ST[i, j] = np.exp(r_t[i, j] + np.log(S0[j]) + (r - q[j] - 0.5 * sigma[j] ** 2) * T)
            payoff[i] = np.maximum(np.max(ST[i, :]) - K, 0)
        option_val.append(np.exp(-r * T) * np.mean(payoff))

        # Bonus 1 requirement - Antithetic variate approach + Moment matching
        z_1 = np.vstack([z[:(n_sim // 2), :], -z[:(n_sim // 2), :]])
        for j in range(n):
            z_1[:, j] = z_1[:, j] / np.std(z_1[:, j])

        r_t = np.matmul(z_1, A)
        for i in range(n_sim):
            for j in range(n):
                ST[i, j] = np.exp(r_t[i, j] + np.log(S0[j]) + (r - q[j] - 0.5 * sigma[j] ** 2) * T)
            payoff[i] = np.maximum(np.max(ST[i, :]) - K, 0)
        option_val_bonus1.append(np.exp(-r * T) * np.mean(payoff))

        # Bonus 2 requirement - Inverse Cholesky decomposition
        cov = np.zeros((n, n))
        for j in range(n):
            for k in range(n):
                cov[j][k] = np.sum((z_1[:, j] - np.mean(z_1[:, j])) * (z_1[:, k] - np.mean(z_1[:, k]))) / (n_sim - 1)
        A_t = cd.Decomposition(cov) 
        A_inv_t = np.linalg.inv(A_t)

        r_t = np.matmul(z_1, np.matmul(A_inv_t, A))
        for i in range(n_sim):
            for j in range(n):
                ST[i, j] = np.exp(r_t[i, j] + np.log(S0[j]) + (r - q[j] - 0.5 * sigma[j] ** 2) * T) 
            payoff[i] = np.maximum(np.max(ST[i, :]) - K, 0)
        option_val_bonus2.append(np.exp(-r * T) * np.mean(payoff))

    option_value = np.mean(option_val)
    option_std = np.std(option_val)
    ci_low = option_value - 2 * option_std
    ci_high = option_value + 2 * option_std

    option_value_bonus1 = np.mean(option_val_bonus1)
    option_std_bonus1 = np.std(option_val_bonus1)
    ci_low_bonus1 = option_value_bonus1 - 2 * option_std_bonus1
    ci_high_bonus1 = option_value_bonus1 + 2 * option_std_bonus1

    option_value_bonus2 = np.mean(option_val_bonus2)
    option_std_bonus2 = np.std(option_val_bonus2)
    ci_low_bonus2 = option_value_bonus2 - 2 * option_std_bonus2
    ci_high_bonus2 = option_value_bonus2 + 2 * option_std_bonus2

    return option_value, ci_low, ci_high, option_value_bonus1, ci_low_bonus1, ci_high_bonus1, option_value_bonus2, ci_low_bonus2, ci_high_bonus2
