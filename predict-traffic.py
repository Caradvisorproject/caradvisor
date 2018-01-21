import requests
from lxml import etree
from datetime import datetime

def predict_points():
    curr_hour = datetime.now().strftime('%H')
    curr_hour = datetime.now().strftime('%H')
    curr_weekday = datetime.now().weekday()
    weekdays = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}
    predict_traff = {0: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0}, 
    1: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0}, 
    2: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0}, 
    3: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0}, 
    4: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0}, 
    5: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:2, 9:3, 10:3, 11:4, 12:5, 13:6, 14:5, 15:6, 16:7, 17:6, 18:7, 19:6, 20:5, 21:4, 22:2, 23:0}, 
    6: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:2, 9:3, 10:3, 11:4, 12:5, 13:6, 14:5, 15:6, 16:7, 17:6, 18:7, 19:6, 20:5, 21:4, 22:2, 23:0}}
    curr_hour = int(curr_hour)
    curr_weekday = int(curr_weekday)
    list_points = []
    if curr_hour == 21:
        list_points.append(int(predict_traff[curr_weekday][22]))
        list_points.append(int(predict_traff[curr_weekday][1]))
        list_points.append(int(predict_traff[curr_weekday][4]))
    elif curr_hour == 22:
        list_points.append(int(predict_traff[curr_weekday][1]))
        list_points.append(int(predict_traff[curr_weekday][4]))
        list_points.append(int(predict_traff[curr_weekday][7]))
    elif curr_hour == 23:
        list_points.append(int(predict_traff[curr_weekday][2]))
        list_points.append(int(predict_traff[curr_weekday][5]))
        list_points.append(int(predict_traff[curr_weekday][8]))
    else:
        list_points.append(int(predict_traff[curr_weekday][curr_hour+3]))
        list_points.append(int(predict_traff[curr_weekday][curr_hour+6]))
        list_points.append(int(predict_traff[curr_weekday][curr_hour+9]))
    return list_points

url = 'https://export.yandex.ru/bar/reginfo.xml?region=213'
result = requests.get(url)
if result.status_code == 200:
    def get_jams():
        tree = etree.fromstring(result.content)
        xpath_tree = tree.xpath('/info/traffic/region/hint/text()')
        return xpath_tree[0]
    
    def get_level():
        tree = etree.fromstring(result.content)
        xpath_tree = tree.xpath('/info/traffic/region/level/text()')
        return xpath_tree[0]

    def get_icon_jams():
        tree = etree.fromstring(result.content)
        xpath_tree = tree.xpath('/info/traffic/region/icon/text()')
        return xpath_tree[0]
else:
    print('Проверьте настройки в модуле!')

def day_type():
    today = datetime.now().weekday()
    weekdays = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}
    if today < 5:
        return 'Сегодня будний день. Пробки обыычно с 7 до 11 и 17 до 21'
    else:
        return 'Сегодня выходной день. Пробки обычно с 11 до 13 и с 17 до 20'

if __name__ == "__main__":
    jams_now = get_jams() + ': ' + get_level() + ' (' + get_icon_jams() + ') '
    jams_predict = 'Предстоящие баллы пробок: ' + str(predict_points())
    day_type = day_type()
    
    print(day_type) '''Вывод рекомендаций по типу дня'''
    print(jams_now) '''Вывод текущих пробок'''
    print(jams_predict) '''Вывод предсказания пробок'''
