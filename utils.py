import datetime
# from src.views import list_transactions
import requests
import os
from pathlib import Path
import requests
from dotenv import load_dotenv
import requests

api = "CGR942J4IU732ZVS"
symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]

# # Initialize an empty list to store stock prices
stock_prices = []

for symbol in symbols:
    # Construct the URL for each symbol
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api}"

    # Make the API request
    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        result = response.json()
        # Access the stock price using the correct key
        stock_data = result.get("Global Quote", {})

        # Get symbol and price from response
        stock_symbol = stock_data.get("01. symbol")
        stock_price = stock_data.get("05. price")

        # Check if symbol and price are available
        if stock_symbol and stock_price:
            stock_prices.append({"stock": stock_symbol, "price": float(stock_price)})
    else:
        print(f"Error {response.status_code}: {response.json().get('Error Message', 'Unknown error')}")

# Assemble the final output
stock = {"stock_prices": stock_prices}
print(stock)