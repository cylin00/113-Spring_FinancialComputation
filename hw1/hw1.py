import optionvalue as ov
import montecarlosimulation as mcs

K1 = 90
K2 = 98
K3 = 102
K4 = 104 #110
S0 = 100 
r = 0.05 
q = 0.02 
sigma = 0.5
T = 0.4

print("Option Price:", ov.option_price(S0, r, q, sigma, T, K1, K2, K3, K4))

ci = mcs.get_95ci(S0, r, q, sigma, T, K1, K2, K3, K4)
print("Mean Price:", ci[0])
print("95% CI: [", ci[1], ", ", ci[2], "]")