from black_scholes import black_scholes
from greeks import calculate_delta
from hedging import delta_neutral_hedge

def main():
    print("🌟 OPTIONS GREEKS CALCULATOR 🌟")
    
    # Ask user for inputs
    S = float(input("Stock Price (S): "))
    K = float(input("Strike Price (K): "))
    T = float(input("Time Left (Years, T): "))
    r = float(input("Interest Rate (e.g., 0.05): "))
    sigma = float(input("Volatility (e.g., 0.20): "))
    option_type = input("Call or Put? ").lower()
    
    # Calculate price and delta
    result = black_scholes(S, K, T, r, sigma, option_type)
    delta = calculate_delta(S, K, T, r, sigma, option_type)
    
    print(f"\n💰 Option Price = ${result['price']:.2f}")
    print(f"Δ Delta = {delta:.4f}")
    
    # Hedging strategy
    hedge_shares = delta_neutral_hedge(delta)
    print(f"\n🛡️ HEDGE: Short {abs(hedge_shares):.2f} shares per option!")

if __name__ == "__main__":
    main()