"""
Monte Carlo valuation of European call option
in Black-Scholes-Merton model
bsm_mcs_euro.py
"""
import math
import numpy as np

# parameter values
S0 = 100        # initial stock index level
K = 105         # strike price of the european call option
T = 1           # time to maturity
R = 0.05        # constant, riskless short rate
SIGMA = 0.2     # constant volatility

# number of simulations
EPOCH = 100000

# valuation algorithm
z = np.random.standard_normal(EPOCH)        # pseudo-random numbers
# index values at maturity
ST = S0 * np.exp((R - SIGMA ** 2 / 2) * T + SIGMA * math.sqrt(T) * z)
hT = np.maximum(ST - K, 0)              # payoff at maturity
C0 = math.exp(-R * T) * np.mean(hT)     # monte carlo estimator

# result output
print(f'Value of the European call option: {C0:5.3f}')
