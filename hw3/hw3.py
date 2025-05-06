import numpy as np

K, r, T = map(float, input("Enter K, r, T: ").split()) # 100 0.02 0.5 
n_sim, n_rep, n = map(int, input("Enter n_sim, n_rep, n: ").split()) # 10000 20 3
S0 = np.array(list(map(int, input(f"Enter [S_10, S_20, ..., S_{n}0]: ").split())))
q = np.array(list(map(float, input(f"Enter [q_1, q_2, ..., q_{n}]: ").split())))
sigma = np.array(list(map(float, input(f"Enter [sigma_1, sigma_2, ..., sigma_{n}]: ").split())))

corr_mat = np.zeros((n, n))
for j in range(n):
    corr_mat[j, :] = list(map(float, input(f"Enter [corr_{j+1}1, corr_{j+1}2, ..., corr_{j+1}{n}]: ").split()))