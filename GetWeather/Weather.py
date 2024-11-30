import requests

Location = input("Please enter the place you want to check weather (Example: Hong Kong): ")
if not Location:
    print("Please enter a valid city or region!")
    exit
if Location.lower() == "hong kong":
    URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    payload = {"dataType":"flw","lang":"tc"}
    response = requests.get(url = URL, params = payload)
    data = response.text
    print(response.url)
    print(data)
else:
    exit