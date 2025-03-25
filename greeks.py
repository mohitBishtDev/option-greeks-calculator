import numpy as np
from scipy.stats import norm

def calculate_delta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return norm.cdf(d1)  # Delta for Call
    else:
        return -norm.cdf(-d1)  # Delta for Put (negative!)