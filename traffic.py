import requests
import datetime
from bs4 import BeautifulSoup

main_yandex = 'http://yandex.ru/'
serp_yandex = 'http://yandex.ru/search/?text=пробки%20сейчас&lr=213'

get_html_main = requests.get(main_yandex)
get_html = requests.get(serp_yandex)

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

'''Работает только ночью'''
def get_jam_night():
    
    bs = BeautifulSoup(get_html_main.content, 'html.parser')
    for item in bs.find_all('a', class_='link traffic__informer traffic__informer-link link_black_yes'):
        JamView = item.text
        return JamView
print('№1 Ночной парсинг: ' + str(get_jam_night()))


'''Работает по выходным'''
def get_jam_day():
    bs = BeautifulSoup(get_html_main.content, 'html.parser')
    for item in bs.find_all('div', class_='traffic__text-forecast traffic__informer'):
        JamView = item.text
        return JamView
print('№2 Парсинг на выходных: ' + str(get_jam_day()))

'''Работает, когда нет пробок'''
def get_jam_day2():
    bs = BeautifulSoup(get_html_main.content, 'html.parser')
    for item in bs.find_all('div', class_='traffic__informer traffic__informer_nojams'):
        JamView = item.text
        return JamView
print('№3 Если нет пробок: ' + str(get_jam_day2()))

'''Парсинг выдачи (вывод баллов)'''
def get_jam_serp():
    bs = BeautifulSoup(get_html.content, 'html.parser')
    for ball in bs.find_all('a', class_='link link_theme_normal i-bem'):
        BallView = ball.text
        return BallView
print('№4 Вывод баллов из выдачи: ' + str(get_jam_serp()))

'''Парсинг выдачи (вывод прогноза)'''
def get_jam_serp_bal():
    bs = BeautifulSoup(get_html.content, 'html.parser')
    for item in bs.find_all('div', class_='traffic-summary__status-text'):
        JamView = item.text
        return JamView
print('№5 Вывод прогноза (текстом) из выдачи: ' + str(get_jam_serp_bal()))
