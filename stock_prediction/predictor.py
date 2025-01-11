# Stock prediction (Linear regression)
# Sklearn https://scikit-learn.org/stable/user_guide.html
# API https://www.alphavantage.co/documentation/
# Matplotlib https://matplotlib.org/stable/users/index.html

import matplotlib.pyplot as plt, numpy as np, pandas as pd, requests
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(stock_code, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&symbol={stock_code}&apikey={api_key}"
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
    prices = [float(v["4. close"]) for v in time_series.values()]
    horizontal = pd.to_datetime(dates)
    vertical = np.array(prices)
    return horizontal, vertical

# Main function
def main():
    api_key = "EL1WRWLWB9B05AS1"
    stock_code = input("Please enter the stock code: ")

    # Fetch stock data
    time_series = fetch_stock_data(stock_code.strip(), api_key)

    # Prepare data
    X_horizontal, y_vertical = prepare_data(time_series)

    # Train the data
    X_train, X_test, y_train, y_test = train_test_split(X_horizontal, y_vertical, test_size=0.25, random_state=42)

    # Perform linear regression
    reg = LinearRegression().fit(np.arange(len(X_train)).reshape(-1, 1), y_train)
    # reg.score(X_horizontal, y_vertical)f

    # Predict
    y_pred = reg.predict(np.arange(len(X_horizontal)).reshape(-1, 1))

    # Plot graph
    plt.figure(figsize=(10, 6))
    # Solid line for actual prices
    plt.plot(X_horizontal, y_vertical, color="blue", label="Actual Prices", linestyle="-")
    # Dotted line for prediction
    plt.plot(X_horizontal, y_pred, color="red", label="Linear Regression Prediction", linestyle="--")
    plt.title(f"Stock Price Prediction for {stock_code}")
    plt.xlabel("Time")
    plt.ylabel("Price")
    # plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()

    # Export and view
    print("Do you want to export the chart as a png or view it? [0 = View it, 1 = Export as png] \n(Please mind that the viewing option won't work if you're using running this code in a web browser)")
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