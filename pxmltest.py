import requests
from lxml import etree

url = 'https://export.yandex.ru/bar/reginfo.xml?region=213'

def get_jams():
    result = requests.get(url)
    if result.status_code == 200:
        tree = etree.fromstring(result.content)
        xpath_tree = tree.xpath('/info/traffic/region/hint/text()')
        return xpath_tree[0]
    else:
        print("Что-то пошло не так")

def get_level():
    result = requests.get(url)
    if result.status_code == 200:
        tree = etree.fromstring(result.content)
        xpath_tree = tree.xpath('/info/traffic/region/level/text()')
        return xpath_tree[0]
    else:
        print("Что-то пошло не так")

def get_icon_jams():
    result = requests.get(url)
    if result.status_code == 200:
        tree = etree.fromstring(result.content)
        xpath_tree = tree.xpath('/info/traffic/region/icon/text()')
        return xpath_tree[0]
    else:
        print("Что-то пошло не так")

if __name__ == "__main__":
    get_jams()
