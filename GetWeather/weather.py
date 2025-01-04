from dotenv import load_dotenv
import requests, os

load_dotenv()

# https://openweathermap.org/api/geocoding-api
# https://openweathermap.org/current
def get_coordinates(city_name):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    geocoding_api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    
    response = requests.get(geocoding_api_url)
    
    if response.status_code != 200 or not response.json():
        print(f"\nCannot find coordinates for {city_name}: {response.status_code} \nTry typing out the full name of the place you want to check!")
        return None, None

    data = response.json()[0]
    print(data["lat"], data["lon"])
    return data["lat"], data["lon"]

def get_uv_index(lat, lon, api_key):
    uv_index_api_url = f"http://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(uv_index_api_url)
    
    if response.status_code != 200:
        print(f"Cannot fetch UV index: {response.status_code}")
        return None

    uv_data = response.json()
    return uv_data["value"]

def get_weather(city_name):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    # Get coordinates for the city
    lat, lon = get_coordinates(city_name)
    if lat is None or lon is None:
        return

    # Fetch the weather data using the coordinates
    openweather_api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(openweather_api_url)
    
    if response.status_code != 200:
        print(f"\nCannot find weather data for {city_name}: {response.status_code} \nTry typing out the full name of the place you want to check!")
        return

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_status = data["weather"][0]["description"]
    uv_index = get_uv_index(lat, lon, api_key)

    print(f"{city_name} Weather:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"UV Index: {uv_index}")
    print(f"Weather Status: {weather_status}")
    print(f"Weather info fetched from OpenWeatherMap API")

# User requests
while True:
    user_input = input("""\nPlease enter the full name of the place you want to check weather (Example: Hong Kong) \nOr type "exit" to quit: """)
    
    if user_input.lower() in ["exit", "q"]:
        print("Exiting...")
        break
    else:
        get_weather(user_input)