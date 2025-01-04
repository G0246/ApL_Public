import matplotlib.pyplot as plt, requests

# Linear regression
# https://scikit-learn.org/stable/user_guide.html
# API https://www.alphavantage.co/documentation/

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=EL1WRWLWB9B05AS1"
r = requests.get(url)
data = r.json()
print(data)
