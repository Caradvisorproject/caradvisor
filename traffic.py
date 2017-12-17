import requests
import datetime
from bs4 import BeautifulSoup

def get_img():
    try:
        response = requests.get('http://static-maps.yandex.ru/1.x/?ll=37.620070,55.753630&spn=0.1,0.1&l=map,trf')
        response.raise_for_status()
        now = datetime.datetime.now()
        filename = "traffic_img/%s.png" % now.strftime("%H-%M-%S--%d-%m-%Y")
        out = open(filename, "wb")
        out.write(response.content)
        out.close()

        traffic_img_name = now.strftime("%H-%M-%S--%d-%m-%Y") + ".png"
        return traffic_img_name
        print('Изображение успешно сохранено в папке')
    except requests.exceptions.RequestException:
        return 'Сервис API Яндекс.Карт недоступен'
'''Вызов функции получения имени изображения get_img()'''



'''get_html = requests.get('http://yandex.ru/search/?text=пробки%20сейчас&lr=213')'''

def get_jam():
    get_html = requests.get('http://yandex.ru/')
    bs = BeautifulSoup(get_html.content, 'html.parser')
    for item in bs.find_all('a', class_='link traffic__informer traffic__informer-link link_black_yes'):
        JamView = item.text
        return JamView
'''Получение пробок с главной страницы'''
