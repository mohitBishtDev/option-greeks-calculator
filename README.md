# Options Greeks Calculator & Hedging Strategy 🌟

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

A simple Python calculator that computes option prices and Greeks using the Black-Scholes model, with delta-neutral hedging capabilities.

## 🧮 Features

- **Option Pricing**: Calculates call/put prices
- **Greeks Calculation**: Currently supports Delta (Δ)
- **Delta Hedging**: Recommends hedge ratios
- **Visualization**: Plots Delta vs. Stock Price

## 🚀 How to Use

 ## Clone the repository:

git clone https://github.com/mohitBishtDev/option-greeks-calculator.git

## Install requirements:

pip install -r requirements.txt

## Run the calculator:

python main.py

## Example output

Stock Price (S): 100
Strike Price (K): 100
Time Left (Years, T): 0.5
Interest Rate (e.g., 0.05): 0.05
Volatility (e.g., 0.20): 0.20
Call or Put? call

## Sample output

💰 Option Price = $9.63
Δ Delta = 0.6376
🛡️ HEDGE: Short 0.64 shares per option!
