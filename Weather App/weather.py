import requests
from dataclasses import dataclass

@dataclass
class WeatherData:
    city_name: str
    country_name: str
    main: str
    description: str
    icon: str
    temperature: float


def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()

    data = resp[0]
    lat , lon = data.get('lat'), data.get('lon')
    city_name, country_name = data.get('name'), data.get('country')
    return lat, lon, city_name, country_name


def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()

    data = WeatherData(
        city_name=resp['name'],
        country_name=resp['sys']['country'],
        main=resp['weather'][0]['main'],
        description=resp['weather'][0]['description'],
        icon=resp['weather'][0]['icon'],
        temperature=resp['main']['temp']
    )
    return data
