import BlackScholes as BS
import MonteCarloSim as MC
import CrrBinomialTree as BT

S0 = 50
K = 50
r = 0.1
q = 0.05
sigma = 0.4
T = 0.5
n_1 = 100
n_2 = 500
n_3 = 10000
num_sim= 10000
num_rep = 30

print("\nBlack-Scholes Formula")
print("European Call Option Value:", BS.GetOptionValue(S0, K, r, q, sigma, T, 'call'))
print("European Put Option Value:", BS.GetOptionValue(S0, K, r, q, sigma, T, 'put'))

print("\nMonte Carlo Simulation")
SimCall = MC.Get95ci(S0, r, q, sigma, T, K, num_sim, num_rep, 'call')
SimPut = MC.Get95ci(S0, r, q, sigma, T, K, num_sim, num_rep, 'put')
print("European Call Option Value:", SimCall[0], ", 95% CI: [", SimCall[1], ", ", SimCall[2], "]")
print("European Put Option Value:", SimPut[0], ", 95% CI: [", SimPut[1], ", ", SimPut[2], "]")

print("\nCRR Binomial Tree - n1")
print("Euprean Call:", BT.GetEuropeanOptionValue(S0, K, r, q, sigma, T, n_1, 'call'), BT.GetEuropean_1D(S0, K, r, q, sigma, T, n_1, 'call'))
print("European Put:", BT.GetEuropeanOptionValue(S0, K, r, q, sigma, T, n_1, 'put'), BT.GetEuropean_1D(S0, K, r, q, sigma, T, n_1, 'put'))
print("American Call:", BT.GetAmericanOptionValue(S0, K, r, q, sigma, T, n_1, 'call'), BT.GetAmerican_1D(S0, K, r, q, sigma, T, n_1, 'call'))
print("American Put:", BT.GetAmericanOptionValue(S0, K, r, q, sigma, T, n_1, 'put'), BT.GetAmerican_1D(S0, K, r, q, sigma, T, n_1, 'put'))

print("\nCRR Binomial Tree - n2")
print("Euprean Call:", BT.GetEuropeanOptionValue(S0, K, r, q, sigma, T, n_2, 'call'), BT.GetEuropean_1D(S0, K, r, q, sigma, T, n_2, 'call'))
print("European Put:", BT.GetEuropeanOptionValue(S0, K, r, q, sigma, T, n_2, 'put'), BT.GetEuropean_1D(S0, K, r, q, sigma, T, n_2, 'put'))
print("American Call:", BT.GetAmericanOptionValue(S0, K, r, q, sigma, T, n_2, 'call'), BT.GetAmerican_1D(S0, K, r, q, sigma, T, n_2, 'call'))
print("American Put:", BT.GetAmericanOptionValue(S0, K, r, q, sigma, T, n_2, 'put'), BT.GetAmerican_1D(S0, K, r, q, sigma, T, n_2, 'put'))

# print("\nCombinatorial Method")
# print("European Call:", BT.GetEuropean_Combinatorial(S0, K, r, q, sigma, T, n_3, 'call'))
# print("European Put:", BT.GetEuropean_Combinatorial(S0, K, r, q, sigma, T, n_3, 'put'), "\n")