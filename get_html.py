import requests


url = 'https://yandex.ru/search/?text=python&lr=213'


def get_html(url):

    try:
        result = requests.get(url)
        return result.text

    except requests.exceptions.RequestException as e:
        print(e)
        return False
