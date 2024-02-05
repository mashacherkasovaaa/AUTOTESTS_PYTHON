# - Проверь, что ответ запрос **GET /trainers** приходит с кодом 200
# - Проверь, что в ответе приходит строчка с именем твоего тренера

import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token':'682033ad89f94a537860edb50519782c'}
CASES = [
    (3773,'MaryChe')
]

def test_get_trainers():
    # get status 200
    response = requests.get(url=f'{URL}/trainers', timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

@pytest.mark.parametrize('id, trainer_name', CASES)

def test_get_trainers_ID(id, trainer_name):
    # Checking the receipt of the trainer's ID
    response = requests.get(f'{URL}/trainers', params={"trainer_id":id}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'
    assert response.json()['trainer_name'] == trainer_name