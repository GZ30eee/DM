# Step 1: Import Libraries
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Step 2: Fetch Stock Price Data
# Define the stock symbol and the time period for which you want to fetch data
stock_symbol = "AAPL"  # Apple stock as an example
start_date = "2020-01-01"
end_date = "2024-01-01"

# Fetch stock data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the first few rows of the data
print(stock_data.head())

# Step 3: Calculate Moving Averages (50-day and 200-day)
# 50-day moving average
stock_data['50_day_MA'] = stock_data['Close'].rolling(window=50).mean()

# 200-day moving average
stock_data['200_day_MA'] = stock_data['Close'].rolling(window=200).mean()

# Step 4: Visualize Stock Prices and Moving Averages
plt.figure(figsize=(14, 8))

# Plotting the closing price
plt.plot(stock_data['Close'], label="Stock Price", color='blue', alpha=0.6)

# Plotting the 50-day moving average
plt.plot(stock_data['50_day_MA'], label="50-Day Moving Average", color='red', alpha=0.8)

# Plotting the 200-day moving average
plt.plot(stock_data['200_day_MA'], label="200-Day Moving Average", color='green', alpha=0.8)

# Add title and labels
plt.title(f"Stock Price Trend Analysis for {stock_symbol}", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Price (USD)", fontsize=14)

# Show legend
plt.legend(loc='upper left')

# Show the plot
plt.grid(True)
plt.show()

# Step 5: Identify Basic Trends (Increasing/Decreasing)
# Check if the stock price is currently above or below the moving averages
latest_price = stock_data['Close'][-1]
latest_50_day_MA = stock_data['50_day_MA'][-1]
latest_200_day_MA = stock_data['200_day_MA'][-1]

print(f"Latest Stock Price: {latest_price}")
print(f"Latest 50-Day Moving Average: {latest_50_day_MA}")
print(f"Latest 200-Day Moving Average: {latest_200_day_MA}")

# Basic trend indication
if latest_price > latest_50_day_MA:
    print("The stock is in an upward trend relative to the 50-day moving average.")
else:
    print("The stock is in a downward trend relative to the 50-day moving average.")

if latest_50_day_MA > latest_200_day_MA:
    print("The stock is in a short-term uptrend compared to the long-term trend.")
else:
    print("The stock is in a short-term downtrend compared to the long-term trend.")
