from crewai.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API = os.getenv("WEATHER_API")

@tool("Weather Information Tool")
def get_weather(city: str) -> str:
    """Fetches real-time weather data for a given city using WeatherAPI."""
    API_KEY = API
    BASE_URL = "https://api.weatherapi.com/v1/current.json"

    url = f"{BASE_URL}?key={API_KEY}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return f"""🌍 **Weather Report for {data['location']['name']}, {data['location']['country']}**
        🌡 Temperature: {data['current']['temp_c']}°C / {data['current']['temp_f']}°F
        💧 Humidity: {data['current']['humidity']}%
        🌬 Wind: {data['current']['wind_kph']} km/h, Direction: {data['current']['wind_dir']}
        ☁ Condition: {data['current']['condition']['text']}
                """

    except requests.exceptions.RequestException as e:
        return f"🚨 Error fetching weather: {e}"
