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
r = 0.05        # constant, riskless short rate
sigma = 0.2     # constant volatility

# number of simulations
I = 100000

# valuation algorithm
z = np.random.standard_normal(I)    # pseudo-random numbers
# index values at maturity
ST = S0 * np.exp((r - sigma ** 2 / 2) * T + sigma * math.sqrt(T) * z)
hT = np.maximum(ST - K, 0)          # payoff at maturity
C0 = math.exp(-r * T) * np.mean(hT) # monte carlo estimator

# result output
print('Value of the European call option: {:5.3f}.'.format(C0))
