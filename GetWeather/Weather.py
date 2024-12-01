from dotenv import load_dotenv
import requests, os

load_dotenv()

# HKOGov API endpoint (Unfinished)
# https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf
def get_hk_weather():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    params = {
        "dataType": "rhrread",
        "lang": "en",
        "r": "1"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if 'current' in data:
            current_weather = data["current"]
            temperature = current_weather.get("temp", "N/A")
            humidity = current_weather.get("humidity", "N/A")
            uv_index = current_weather.get("uvIndex", "N/A")
            weather_status = current_weather.get("weather", "N/A")

            print("Current Weather in Hong Kong:")
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")
            print(f"UV Index: {uv_index}")
            print(f"Weather Status: {weather_status}")
        else:
            print("Unexpected response structure:", data)

    except requests.exceptions.RequestException as e:
        print("Error fetching data from HKO API:", e)

 # OpenWeatherMap API Example
def get_weather(city_name):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    openweather_api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(openweather_api_url)
    
    if response.status_code != 200:
        print(f"\nCannot find weather data for {city_name}: {response.status_code} \nTry typing out the full name of the place you want to check!")
        return

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_status = data["weather"][0]["description"]
    uv_index = get_uv_index(data["coord"]["lat"], data["coord"]["lon"], api_key)

    print(f"{city_name} Weather:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"UV Index: {uv_index}")
    print(f"Weather Status: {weather_status}")
    print(f"Weather info fetched from OpenWeatherMap API")

# OpenWeatherMap UV Index
def get_uv_index(lat, lon, api_key):
    uv_api_url = f"http://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(uv_api_url)
    uv_data = response.json()
    return uv_data["value"]

# User requests
while True:
    user_input = input("""\nPlease enter the full name of the place you want to check weather (Example: Hong Kong) \nOr type "exit" to quit: """)
    
    if user_input.lower() in ["exit", "q"]:
        print("Exiting...")
        break
    elif user_input.lower() in ["hong kong", "hk"]:
        # get_hk_weather()
        get_weather(user_input)
    else:
        get_weather(user_input)