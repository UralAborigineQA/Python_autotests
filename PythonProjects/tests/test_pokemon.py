import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'тут должен быть твой токен'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRA_ID = 4125


def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200


def test_trainer_id():
    response_get = requests.get(
        url=f'{URL}/trainers', params={'trainer_id': TRA_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Человек'
