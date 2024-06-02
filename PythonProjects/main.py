import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'тут должен быть твой токен'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo": "generate"
}

body_name = {
    "pokemon_id": "26527",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_ball = {
    "pokemon_id": "26528"
}

response = requests.post(url=f'{URL}/pokemons',
                         headers=HEADER, json=body_create)
print(response.text)

response = requests.put(url=f'{URL}/pokemons',
                        headers=HEADER, json=body_name)
print(response.text)

response = requests.post(url=f'{URL}/trainers/add_pokeball',
                         headers=HEADER, json=body_ball)
print(response.text)
