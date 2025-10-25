import requests

API_KEY = "0cfd2731569f30c734852ccb773b25bb"

api_url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=New York"

def fetch_data():
    print("Fetching weather data from WeatherStack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"A error occured on the API call: {e}")
        raise

fetch_data()
#def mock_fetch_data():
#   return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-10-22 02:09', 'localtime_epoch': 1761098940, 'utc_offset': '-4.0'}, 'current': {'observation_time': '06:09 AM', 'temperature': 15, 'weather_code': 296, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0033_cloudy_with_light_rain_night.png'], 'weather_descriptions': ['Light Rain'], 'astro': {'sunrise': '07:15 AM', 'sunset': '06:05 PM', 'moonrise': '08:26 AM', 'moonset': '06:19 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 0}, 'air_quality': {'co': '188.85', 'no2': '29.35', 'o3': '52', 'so2': '7.55', 'pm2_5': '10.75', 'pm10': '10.75', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 9, 'wind_degree': 207, 'wind_dir': 'SSW', 'pressure': 1010, 'precip': 1, 'humidity': 83, 'cloudcover': 100, 'feelslike': 15, 'uv_index': 0, 'visibility': 11, 'is_day': 'no'}}