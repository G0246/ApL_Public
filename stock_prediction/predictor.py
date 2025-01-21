# Stock prediction program (UNFINISHED)
# Code is rebased on 19/01/24

# Sklearn https://scikit-learn.org/stable/user_guide.html
# API https://www.alphavantage.co/documentation/
# Matplotlib https://matplotlib.org/stable/users/index.html

# Import libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Function to fetch data from Alpha Vantage API
def fetch_stock_data(stock_code, start_date, end_date, api_key):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_code,
        "outputsize": "full",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Check if data is valid
    if "Time Series (Daily)" not in data:
        raise ValueError("Invalid stock code or API limit exceeded")
    
    # Convert JSON to DataFrame
    time_series = data["Time Series (Daily)"]
    df = pd.DataFrame.from_dict(time_series, orient="index", dtype=float)
    df = df.rename(columns={"4. close": "close"})
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    
    # Filter by date range
    return df.loc[start_date:end_date]["close"]

api_key = "EL1WRWLWB9B05AS1"
stock_code = input("Enter the stock code (e.g., AAPL): ").upper().strip()
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# MAIN FUNCTION
try:
    # Fetch stock data
    stock_prices = fetch_stock_data(stock_code, start_date, end_date, api_key)

    # Prepare data for modeling
    dates = np.arange(len(stock_prices)).reshape(-1, 1)
    prices = stock_prices.values

    # Scaling data
    scaler = MinMaxScaler()
    prices_scaled = scaler.fit_transform(prices.reshape(-1, 1))

    # Linear regression
    linear_model = LinearRegression()
    linear_model.fit(dates, prices_scaled)
    linear_pred = linear_model.predict(dates)

    # Polynomial regression (degree 3)
    poly_features = PolynomialFeatures(degree=3)
    dates_poly = poly_features.fit_transform(dates)
    poly_model = LinearRegression()
    poly_model.fit(dates_poly, prices_scaled)
    poly_pred = poly_model.predict(dates_poly)

    # Metrics
    linear_mse = mean_squared_error(prices_scaled, linear_pred)
    linear_r2 = r2_score(prices_scaled, linear_pred)
    poly_mse = mean_squared_error(prices_scaled, poly_pred)
    poly_r2 = r2_score(prices_scaled, poly_pred)

    # Rescale predictions back to original range
    linear_pred_rescaled = scaler.inverse_transform(linear_pred)
    poly_pred_rescaled = scaler.inverse_transform(poly_pred)

    # Plotting the data
    plt.figure(figsize=(12, 6))
    plt.plot(stock_prices.index, prices, label="Actual Prices (Full)", color="blue")
    plt.plot(stock_prices.index, linear_pred_rescaled, label="Linear Regression", linestyle="--", color="green")
    plt.plot(stock_prices.index, poly_pred_rescaled, label="Polynomial Regression", linestyle=":", color="red")
    plt.title(f"{stock_code} Stock Prices: Actual, Trends, and Predictions")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    # Ask the user whether to view or export the graph
    choice = input("Would you like to view the plot or save it as a PNG? (view/save): ").strip().lower()

    if choice == "view":
        plt.show()
    elif choice == "save":
        plt.savefig(f"{stock_code}_prediction.png")
        print(f"Plot saved as {stock_code}_prediction.png")
    else:
        print("Invalid choice. Operation cancelled.")

    # Print metrics
    print(f"\nMetrics:")
    print(f"Linear Regression MSE: {linear_mse:.4f}, R²: {linear_r2:.4f}")
    print(f"Polynomial Regression MSE: {poly_mse:.4f}, R²: {poly_r2:.4f}")

except Exception as e:
    print(f"Error: {e}")
