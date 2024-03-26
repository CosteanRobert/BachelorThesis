import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the previously saved data
data = pd.read_csv('AAPL_stock_data_with_indicators.csv')

# Selecting only the numerical columns for the correlation matrix
numerical_data = data[['Close', 'Volume', 'MACD', 'Signal_Line', 'RSI', 'Middle_Band', 'Upper_Band', 'Lower_Band']]

# Calculate the correlation matrix
corr_matrix = numerical_data.corr()

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='viridis', cbar=True, square=True)
plt.title('Correlation Matrix for AAPL Stock Data with Indicators')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()
