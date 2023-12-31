import finnhub
import pandas as pd
import datetime
import alpaca_trade_api as tradeapi

# Finnhub API Key
FINNHUB_API_KEY = 'your_finnhub_api_key'

# Initialize Finnhub client
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

# Define your Alpaca API credentials
API_KEY = 'your_alpaca_api_key'
API_SECRET = 'your_alpaca_api_secret'
BASE_URL = 'https://paper-api.alpaca.markets'

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL)

# Function to get active stocks
def get_active_stocks():
    # Fetch list of market movers or active stocks from Finnhub
    movers = finnhub_client.general_news('general', min_id=0)
    symbols = [item['symbol'] for item in movers if 'symbol' in item]
    return symbols

# Function to analyze stock
# ... [rest of the analyze_stock function as before]

# Function for trading logic
# ... [rest of the trade_logic function as before]

# Function to execute trades
def execute_trade(symbol, decision):
    if decision == 'buy':
        api.submit_order(symbol=symbol, qty=1, side='buy', type='market', time_in_force='gtc')
    elif decision == 'sell':
        api.submit_order(symbol=symbol, qty=1, side='sell', type='market', time_in_force='gtc')

# Get active stocks
active_stocks = get_active_stocks()

# Loop through each active stock and execute trades
for symbol in active_stocks:
    decision = analyze_stock(symbol)
    execute_trade(symbol, decision)
