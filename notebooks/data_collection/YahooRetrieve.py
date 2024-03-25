import yfinance as yf
import pandas as pd

# Define stock symbols and time range
symbols = ['AAPL', 'MSFT', 'AMD']
start_date = '2020-01-01'
end_date = '2022-01-01'

# Fetch historical stock market data
data = yf.download(symbols, start=start_date, end=end_date)

# Print columns in the data DataFrame
print("Columns in data DataFrame:")
print(data.columns)

# Create an empty DataFrame to store calculated data
result_data = pd.DataFrame()

# Calculate technical indicators for each stock
for symbol in symbols:
    for price_type in ['Close', 'Volume']:  # Only need Close and Volume
        col_name = (price_type, symbol)
        if col_name not in data.columns:
            print(f"Column {col_name} not found for {symbol}. Skipping...")
            continue
        
        stock_data = data[col_name].copy()  # Access stock data by ticker symbol
        
        # Calculate Simple Moving Average (SMA) for 50 days
        stock_data[f'{symbol}_SMA_50'] = stock_data.rolling(window=50).mean()
        
        # Concatenate the calculated data for this stock with the result DataFrame
        result_data = pd.concat([result_data, stock_data], axis=1)

# Print the first few rows of the result DataFrame
print("\nResulting DataFrame:")
print(result_data.head())

result_data.to_csv('stock_data.csv')
