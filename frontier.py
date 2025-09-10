import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# 1. Portfolio setup
# -----------------------------
tickers = ["THYAO.IS", "ASELS.IS", "GARAN.IS"]
weights = np.array([0.4, 0.3, 0.3])

# -----------------------------
# 2. Download data
# -----------------------------
raw_data = yf.download(tickers, start="2023-01-01", end="2025-01-01")
data = raw_data["Close"]

# daily returns
returns = data.pct_change().dropna()

# annualized stats
annual_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

# -----------------------------
# 3. Portfolio metrics function
# -----------------------------
def portfolio_performance(weights, mean_returns, cov_matrix):
    port_return = np.dot(weights, mean_returns)
    port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return port_return, port_volatility

# -----------------------------
# 4. Monte Carlo Simulation
# -----------------------------
num_portfolios = 10000
results = np.zeros((3, num_portfolios))  # return, volatility, sharpe

for i in range(num_portfolios):
    # random weights
    w = np.random.random(len(tickers))
    w /= np.sum(w)

    ret, vol = portfolio_performance(w, annual_returns, cov_matrix)
    sharpe = ret / vol

    results[0,i] = ret
    results[1,i] = vol
    results[2,i] = sharpe

# -----------------------------
# 5. Your chosen portfolio
# -----------------------------
my_return, my_volatility = portfolio_performance(weights, annual_returns, cov_matrix)
my_sharpe = my_return / my_volatility

print("Expected Annual Portfolio Return:", round(my_return*100, 2), "%")
print("Annual Volatility (Risk):", round(my_volatility*100, 2), "%")
print("Sharpe Ratio:", round(my_sharpe, 2))

# -----------------------------
# 6. Visualization
# -----------------------------
plt.figure(figsize=(10,7))
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap="viridis", s=10)
plt.colorbar(label="Sharpe Ratio")
plt.scatter(my_volatility, my_return, c="red", marker="*", s=200, label="My Portfolio")
plt.xlabel("Volatility (Risk)")
plt.ylabel("Expected Return")
plt.title("Efficient Frontier with Random Portfolios")
plt.legend()
plt.show()


"""
“I coded a Monte Carlo simulation of 10,000 random BIST portfolios in Python. It calculates risk, return, and Sharpe ratio for each, and plots the Efficient Frontier. This gave me practical insight into diversification, risk-adjusted returns, and portfolio optimization, which connects directly to SPL concepts.”
"""