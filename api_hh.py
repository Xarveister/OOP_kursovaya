from pprint import pprint

import requests

# Список id работодателей

employers_ids = [
    1235466,
    9122212,
    4394271,
    151875,
    5904250,
    5688132,
    804442,
    3344436,
    2978155,
    4945143
]

# функция получения данных с сайта HH.ru

url = "https://api.hh.ru/vacancies?employer_id="
params = {"pages": 100, "per_page": 10, "only_with_vacancies": True}


def API_hh():
    """Функция для подключения к api hh.ru"""
    data = []
    for employers_id in employers_ids:
        response = requests.get(f"{url}{employers_id}", params=params)
        if response.status_code != 200:
            pprint(f"Connection error with code {response.status_code}")
        else:
            data.append(response.json()['items'])

    return data



