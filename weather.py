from get_weather import get_weather
from weather_settings import API_KEY


current_weather = get_weather('http://api.openweathermap.org/data/2.5/weather?id=524901&units=metric&appid=%s' % (API_KEY))
print(current_weather)
