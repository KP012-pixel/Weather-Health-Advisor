from dotenv import load_dotenv
from weather import get_weather, analyze_weather, display_health_advice
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")  # Fetch the API key from .env
if API_KEY is None:
    raise ValueError("API_KEY is not set in the .env file!")

if __name__ == "__main__":
    city = input("Enter city name: ")

    # Fetch weather data using get_weather function
    weather_data = get_weather(city, API_KEY)

    if weather_data["cod"] == 200:
        advice = analyze_weather(weather_data)
        display_health_advice(weather_data, advice)
    else:
        print("City not found! Please check your input.")
