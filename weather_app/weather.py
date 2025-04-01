import requests
from dotenv import load_dotenv
import os
from pprint import pprint
weather_data = {"base": "stations",
 "clouds": {"all": 75},
 "cod": 200,
 "coord": {"lat": 30.7835, "lon": -88.2},
 "dt": 1743543272,
 "id": 4076607,
 "main": {"feels_like": 78.84,
          "grnd_level": 1007,
          "humidity": 67,
          "pressure": 1013,
          "sea_level": 1013,
          "temp": 78.17,
          "temp_max": 79.75,
          "temp_min": 75.56},
 "name": "Mobile",
 "sys": {"country": "US",
         "id": 4948,
         "sunrise": 1743507677,
         "sunset": 1743552692,
         "type": 1},
 "timezone": -18000,
 "visibility": 10000,
 "weather": [{"description": "broken clouds",
              "icon": "04d",
              "id": 803,
              "main": "Clouds"}],
 "wind": {"deg": 150, "speed": 11.5}}

load_dotenv()

def get_current_weather():
    print("\n***Get Current Weather Conditions***\n")

    city = input("\nPlease enter a city name:\n")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"

    #uncomment when ready to make real API calls
    #weather_data = requests.get(request_url).json()

    print(f"\nCurrent weather for {weather_data["name"]}:")
    print(f"\nThe Temp is {weather_data["main"]["temp"]}")
    print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.")
    pprint(weather_data)


if __name__ == "__main__":
    get_current_weather()