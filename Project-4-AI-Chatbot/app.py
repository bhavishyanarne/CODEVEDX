import requests
import json
from datetime import datetime

# Weather API Configuration
API_KEY = "your_api_key_here"  # Get free key from openweathermap.org
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather data for a given city
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use Celsius
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    """
    Display weather information in a formatted manner
    """
    if not data:
        print("Could not fetch weather data.")
        return
    
    city = data.get('name')
    country = data.get('sys', {}).get('country')
    temp = data.get('main', {}).get('temp')
    feels_like = data.get('main', {}).get('feels_like')
    humidity = data.get('main', {}).get('humidity')
    pressure = data.get('main', {}).get('pressure')
    description = data.get('weather', [{}])[0].get('description')
    wind_speed = data.get('wind', {}).get('speed')
    
    print("\n" + "="*50)
    print(f"🌍 Weather Dashboard - {city}, {country}")
    print("="*50)
    print(f"📅 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌡️  Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"💧 Humidity: {humidity}%")
    print(f"🔽 Pressure: {pressure} hPa")
    print(f"☁️  Conditions: {description.capitalize()}")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print("="*50 + "\n")

def get_forecast(city):
    """
    Fetch 5-day forecast (requires paid API or different endpoint)
    """
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(forecast_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None

def main():
    """
    Main function to run the weather dashboard
    """
    print("\n🌤️  Weather Dashboard Application")
    print("-" * 50)
    
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        if city.lower() == 'quit':
            print("\nThank you for using Weather Dashboard! Goodbye! 👋")
            break
        
        if not city:
            print("Please enter a valid city name.")
            continue
        
        print(f"\nFetching weather data for {city}...")
        weather_data = get_weather(city)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
