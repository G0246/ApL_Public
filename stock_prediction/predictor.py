# Stock prediction (Linear regression)
# https://scikit-learn.org/stable/user_guide.html
# API https://www.alphavantage.co/documentation/

import matplotlib.pyplot as plt, numpy as np, requests
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(stock_code, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_code}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "Time Series (Daily)" in data:
        return data["Time Series (Daily)"]
    else:
        print("Invalid stock code. Unable to fetch data.")
        exit()

# Prepare data
def prepare_data(time_series):
    times = list(range(len(time_series)))
    prices = [float(v["4. close"]) for v in time_series.values()]
    horizontal = np.array(times).reshape(-1, 1)
    vertical = np.array(prices)
    return horizontal, vertical

# Main function
def main():
    # Do not disclose
    api_key = "EL1WRWLWB9B05AS1"
    stock_code = input("Please enter the stock code: ")

    # Fetch stock data
    time_series = fetch_stock_data(stock_code.strip(), api_key)

    # Prepare data
    X, y = prepare_data(time_series)

    # Train the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    # Perform linear regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X)

    # Plot graph
    plt.figure(figsize=(10, 6))
    plt.plot(X, y, color="blue", label="Actual Prices", linestyle="-")  # Solid line for actual prices
    plt.plot(X, y_pred, color="red", label="Linear Regression Prediction", linestyle="--")  # Dotted line for prediction
    plt.title(f"Stock Price Prediction for {stock_code}")
    plt.xlabel("Time (indices)")
    plt.ylabel("Price")
    plt.legend()

    # Export
    output_file = f"{stock_code}_prediction.png"
    plt.savefig(output_file)
    print(f"Prediction chart saved as {output_file}")

if __name__ == "__main__":
    main()
