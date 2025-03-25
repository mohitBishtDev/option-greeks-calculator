def delta_neutral_hedge(delta, num_options=1):
    """
    delta = Delta of the option (e.g., 0.6)
    num_options = How many options you have (default: 1)
    """
    return -delta * num_options  # Negative means SELL shares!