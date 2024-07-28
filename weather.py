import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    print('\n***Get current weather conditions***\n'.upper())
    city = input('\nplease enter a city name\n')
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]} and country is {weather_data["sys"]["country"]}')


if __name__ == "__main__":
    get_current_weather()

















# {'base': 'stations',
#  'clouds': {'all': 1},
#  'cod': 200,
#  'coord': {'lat': 30.0081, 'lon': 31.2109},
#  'dt': 1722140831,
#  'id': 360995,
#  'main': {'feels_like': 26.41,
#           'grnd_level': 1004,
#           'humidity': 64,
#           'pressure': 1010,
#           'sea_level': 1010,
#           'temp': 26.41,
#           'temp_max': 26.41,
#           'temp_min': 25.78},
#  'name': 'Giza',
#  'sys': {'country': 'EG',
#          'id': 2514,
#          'sunrise': 1722136306,
#          'sunset': 1722185478,
#          'type': 1},
#  'timezone': 10800,
#  'visibility': 10000,
#  'weather': [{'description': 'clear sky',
#               'icon': '01d',
#               'id': 800,
#               'main': 'Clear'}],
#  'wind': {'deg': 353, 'gust': 4.28, 'speed': 3.65}}