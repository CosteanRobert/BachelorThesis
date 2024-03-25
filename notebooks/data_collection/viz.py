import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data from the CSV file
stock_data = pd.read_csv('stock_data.csv', index_col=0, parse_dates=True)

# Plotting parameters
plt.figure(figsize=(12, 8))

# Plot closing prices for AAPL
plt.plot(stock_data.index[:10], stock_data["('Close', 'AAPL')"][:10], label='AAPL Close', color='blue', marker='o')

# Set plot title and labels
plt.title('AAPL Closing Prices (First 10 Data Points)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
