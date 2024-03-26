import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('AAPL_stock_data_with_indicators.csv', index_col='Date', parse_dates=True)

# Plotting
fig, axs = plt.subplots(4, 1, figsize=(12, 20))

# Closing Price Plot
axs[0].plot(data['Close'], label='Close Price', color='blue')
axs[0].set_title('AAPL Close Price')
axs[0].legend()

# MACD Plot
axs[1].plot(data['MACD'], label='MACD', color='green')
axs[1].plot(data['Signal_Line'], label='Signal Line', color='red')
axs[1].set_title('AAPL MACD')
axs[1].legend()

# RSI Plot
axs[2].plot(data['RSI'], label='RSI', color='purple')
axs[2].set_title('AAPL RSI')
axs[2].axhline(70, linestyle='--', color='red')
axs[2].axhline(30, linestyle='--', color='green')
axs[2].legend()

# Bollinger Bands Plot
axs[3].plot(data['Close'], label='Close', color='blue')
axs[3].plot(data['Upper_Band'], label='Upper Band', linestyle='--', color='orange')
axs[3].plot(data['Middle_Band'], label='Middle Band', linestyle='--', color='black')
axs[3].plot(data['Lower_Band'], label='Lower Band', linestyle='--', color='orange')
axs[3].set_title('AAPL Bollinger Bands')
axs[3].legend()

for ax in axs:
    ax.grid(True)

plt.tight_layout()
plt.show()
