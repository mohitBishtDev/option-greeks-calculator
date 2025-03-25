# We need these tools to do math
import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    S = Stock Price (like $100)
    K = Strike Price (like $110)
    T = Time left (like 1 year)
    r = Interest Rate (like 0.05 for 5%)
    sigma = How crazy the stock moves (like 0.20 for 20%)
    option_type = "call" (bet stock goes up) or "put" (bet stock goes down)
    """
    # Step 1: Calculate d1 and d2 (magic numbers)
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Step 2: Calculate Call or Put price
    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)  # How much price changes when stock moves
    else:  # Put option
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = -norm.cdf(-d1)
    
    return {'price': price, 'delta': delta}