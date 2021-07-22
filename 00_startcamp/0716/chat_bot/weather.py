import requests
from telegram import sendMessage

def checkWeather(location_name):
    url = 'https://www.metaweather.com/'
    location_search_url = 'api/location/search/?query='

    location_response = requests.get(url + location_search_url + location_name).json()
    woeid = location_response[0]['woeid']

    location_url = '/api/location/' + str(woeid)
    response = requests.get(url + location_url).json()

    weather = response['consolidated_weather'][2]['weather_state_name']

    weather_translater = {
        'Snow' : '눈',
        'Sleet' : '진눈깨비',
        'Hail' : '우박',
        'Thunderstorm' : '뇌우',
        'Heavy Rain' : '강우',
        'Light Rain' : '비',
        'Showers' : '소나기',
        'Heavy Cloud' : '흐림',
        'Light Cloud' : '구름조금',
        'Clear' : '맑음',
    }
    return weather_translater[weather]

weather = checkWeather('seoul')
weather_msg = f'서울의 모레 날씨는 {weather}(으)로 예상됩니다.'
sendMessage(weather_msg)