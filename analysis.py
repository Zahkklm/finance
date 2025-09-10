import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tickers = ["THYAO.IS", "ASELS.IS", "GARAN.IS"]
weights = np.array([0.4, 0.3, 0.3])

# download data (yfinance now returns adjusted prices in "Close")
raw_data = yf.download(tickers, start="2023-01-01", end="2025-01-01")

# use "Close" instead of "Adj Close"
data = raw_data["Close"]

# daily returns
returns = data.pct_change().dropna()

# expected annual return
annual_returns = returns.mean() * 252
portfolio_return = np.dot(weights, annual_returns)

# covariance matrix (risk)
cov_matrix = returns.cov() * 252
portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Sharpe ratio (risk-free = 0 for simplicity)
sharpe_ratio = portfolio_return / portfolio_volatility

print("Expected Annual Portfolio Return:", round(portfolio_return*100, 2), "%")
print("Annual Volatility (Risk):", round(portfolio_volatility*100, 2), "%")
print("Sharpe Ratio:", round(sharpe_ratio, 2))

# plot cumulative returns
plt.figure(figsize=(10,6))
(1 + returns).cumprod().plot()
plt.title("Cumulative Returns of Portfolio Assets", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Growth of 1 TL")
plt.legend(tickers)
plt.show()
