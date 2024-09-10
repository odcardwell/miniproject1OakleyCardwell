# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the 'charts' folder exists
if not os.path.exists('charts'):
    os.makedirs('charts')

# List of your favorite stock tickers
tickers = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'NVDA']

# Get data for the last 1 month for each ticker and slice to last 10 trading days
stock_data = {}
for ticker in tickers:
    stock = yf.Ticker(ticker)
    history = stock.history(period='1mo')['Close']  # Get 1 month of data
    stock_data[ticker] = history[-10:]  # Slice the last 10 days

# Convert stock data into a NumPy array and plot the data
for ticker, data in stock_data.items():
    np_data = np.array(data)

    # Create a plot for the stock data
    plt.figure()
    plt.plot(np_data, marker='o', linestyle='-', color='b')
    plt.title(f'{ticker} Stock Price - Last 10 Days')
    plt.xlabel('Days')
    plt.ylabel('Closing Price (USD)')
    plt.grid(True)

    # Save the plot as a PNG file in the 'charts' folder
    plt.savefig(f'charts/{ticker}_chart.png')

# Print a message once the graphs have been saved
print("All charts have been saved in the 'charts' folder.")