import requests
import json

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def load_exchange():
    response = requests.get(URL)
    return json.loads(response.text)['Valute']


def get_exchange(key):
    for item in load_exchange():
        if key == item:
            data = load_exchange()[item]
            return data['Name'], data['Value']


def get_currencies():
    return [item for item in load_exchange()]
