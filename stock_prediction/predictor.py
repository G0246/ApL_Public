import matplotlib.pyplot as plt, requests

# API
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=EL1WRWLWB9B05AS1"
r = requests.get(url)
data = r.json()
print(data)
