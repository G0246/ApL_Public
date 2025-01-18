# Stock prediction using Linear Regression
# Sklearn https://scikit-learn.org/stable/user_guide.html
# API https://www.alphavantage.co/documentation/
# Matplotlib https://matplotlib.org/stable/users/index.html

import matplotlib.pyplot as plt
import numpy as np
import requests
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(stock_code):
    api_key = "EL1WRWLWB9B05AS1"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&symbol={stock_code}&apikey={api_key}&outputsize=full"
    response = requests.get(url)
    data = response.json()
    if "Time Series (Daily)" in data:
        return data["Time Series (Daily)"]
    else:
        print("Invalid stock code. Unable to fetch data.")
        exit()

# Prepare data
def prepare_data(time_series):
    dates = list(time_series.keys())
    prices = [float(v["4. close": "Close"]) for v in time_series.values()]
    X = pd.to_datetime(dates)
    y = np.array(prices)
    return X, y

start_plot_date = input()
end_plot_date = input()