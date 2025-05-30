import numpy as np
import Simulation as sim

# --------- Inputs ---------

K, r, T = map(float, input("Enter K, r, T: ").split()) 
n_sim, n_rep, n = map(int, input("Enter n_sim, n_rep, n: ").split()) 
S0 = np.array(list(map(int, input(f"Enter [S_10, S_20, ..., S_{n}0]: ").split())))
q = np.array(list(map(float, input(f"Enter [q_1, q_2, ..., q_{n}]: ").split())))
sigma = np.array(list(map(float, input(f"Enter [sigma_1, sigma_2, ..., sigma_{n}]: ").split())))

corr = np.zeros((n, n))
for j in range(n):
    corr[j, :] = list(map(float, input(f"Enter [corr_{j+1}1, corr_{j+1}2, ..., corr_{j+1}{n}]: ").split()))

# --------- Outputs ---------
    
a, l, h, a_1, l_1, h_1, a_2, l_2, h_2 = sim.GetOptionValue(K, r, T, n_sim, n_rep, n, S0, q, sigma, corr)
print(f"Basic -  Mean: {a:.5f}, 95% CI: [{l:.5f}, {h:.5f}], range ~ {(h - l):.5f}")
print(f"Bonus1 - Mean: {a_1:.5f}, 95% CI: [{l_1:.5f}, {h_1:.5f}], range ~ {(h_1 - l_1):.5f}")
print(f"Bonus2 - Mean: {a_2:.5f}, 95% CI: [{l_2:.5f}, {h_2:.5f}], range ~ {(h_2 - l_2):.5f}")