# Stock prediction using Linear Regression
# Sklearn https://scikit-learn.org/stable/user_guide.html
# API https://www.alphavantage.co/documentation/
# Matplotlib https://matplotlib.org/stable/users/index.html

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(stock_code):
    api_key = "EL1WRWLWB9B05AS1"  # Replace with your own API key
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
    horizontal = pd.to_datetime(dates)
    vertical = np.array(prices)
    return horizontal, vertical

# Main function
def main():
    stock_code = input("Please enter the stock code: ").strip().upper()
    time_series = fetch_stock_data(stock_code)

    # Prepare data
    X_horizontal, y_vertical = prepare_data(time_series)

    # Reshape the data for the model
    X = np.arange(len(X_horizontal)).reshape(-1, 1)  # Use the index as the feature
    y = y_vertical.reshape(-1, 1)

    # Scale the data
    scaler_X = MinMaxScaler()
    scaler_y = MinMaxScaler()
    X_scaled = scaler_X.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y)

    # Fit the model
    model = LinearRegression()
    model.fit(X_scaled, y_scaled)

    # Predict on the original data
    y_pred_scaled = model.predict(X_scaled)
    y_pred = scaler_y.inverse_transform(y_pred_scaled)

    # Evaluate the model
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    print(f"均方誤差 (MSE): {mse}")
    print(f"決定係數 (R²): {r2}")

    # Predict future months (Not working)
    future_months = 3
    future_x = np.arange(len(X_horizontal), len(X_horizontal) + future_months).reshape(-1, 1)
    future_x_scaled = scaler_X.transform(future_x)
    future_y_pred_scaled = model.predict(future_x_scaled)
    future_y_pred = scaler_y.inverse_transform(future_y_pred_scaled)

    # Combine actual and predicted data
    X_future = pd.date_range(start=X_horizontal[-1] + pd.Timedelta(days=1), periods=future_months, freq='B')  # Business days

    # Plot graph
    plt.figure(figsize=(10, 6), facecolor="white", layout="constrained")
    # Solid line for actual prices
    plt.plot(X_horizontal, y_vertical, color="blue", label="Actual Prices", linestyle="-")
    # Dotted line for prediction
    plt.plot(X_horizontal, y_pred, color="red", label="Linear Regression Prediction", linestyle="--")
    # Future predictions
    plt.plot(X_future, future_y_pred, color="green", label="Future Predictions", linestyle="--")
    plt.title(f"Stock Price Prediction for {stock_code}")
    plt.xlabel("Time")
    plt.ylabel("Price")
    # plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()

    # Export and view
    print("Do you want to export the chart as a png or view it? [0 = View it, 1 = Export as png]")
    choice = int(input("Please input your choice: "))
    if choice == 0:
        plt.show()
    elif choice == 1:
        output_file = f"{stock_code}_prediction.png"
        plt.savefig(output_file)
        print(f"Prediction chart saved as {output_file}")
    else:
        print("Invalid choice!")
        exit()

if __name__ == "__main__":
    main()