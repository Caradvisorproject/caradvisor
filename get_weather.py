import requests

from settings import OPENWEATHER_API_KEY


def get_weather_data():
    """Getting current weather"""
    url = 'http://api.openweathermap.org/data/2.5/weather?id=524901&units=metric&lang=ru&appid=%s' % (OPENWEATHER_API_KEY)

    try:
        result = requests.get(url)
    except requests.exceptions.RequestException as e:
        print('Exception happend: ', e)

    if result.status_code == 200:
        return result.json()
    else:
        print('Somthg is wrong with server response')


def get_weather_message():
    """Returns current weather conditions message"""
    data = get_weather_data()
    weather_message = ''
    weather_message += 'Тек. темп = {} \xB0C (Max = {} \xB0С, Min = {} \xB0C)'.format(data['main']['temp'], data['main']['temp_max'], data['main']['temp_min'])
    weather_message += '\nПогодные усл. - {}, видимость - {} м,\nВетер - {} м/с, облачность {}%'.format(data['weather'][0]['description'], data['visibility'], data['wind']['speed'], data['clouds']['all'])
    return weather_message

if __name__ == '__main__':
    #data = get_weather_data()
    #print('{}, maxtemp = {}, mintemp = {}. Current temp = {}'.format(data['name'], data['main']['temp_max'], data['main']['temp_min'], data['main']['temp']))
    #print('\nПогодные усл. - {}, видимость - {} м, ветер - {} м/с, облачность {}%'.format(data['weather'][0]['description'], data['visibility'], data['wind']['speed'], data['clouds']['all']))
    print(type(get_weather_data()))

