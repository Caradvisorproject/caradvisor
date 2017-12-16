import requests
import datetime

def GetTraffic():
    response = requests.get('http://static-maps.yandex.ru/1.x/?ll=37.620070,55.753630&spn=0.1,0.1&l=map,trf')
    now = datetime.datetime.now()
    filename = "traffic_img/%s.png" % now.strftime("%H-%M-%S--%d-%m-%Y")
    out = open(filename, "wb")
    out.write(response.content)
    out.close()

    traffic_img_name = now.strftime("%H-%M-%S--%d-%m-%Y") + ".png"
    return(traffic_img_name)

def GetNumTraffic():
    pass
'''Имя фотографии передается в переменную traffic_img_name'''
'''Для вызова функции вызови GetTraffic()'''