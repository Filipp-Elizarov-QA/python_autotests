import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN ='bc523580e6a93e6d8013f33b64e7fb78'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
body_create = {
    "name": "Zaba123",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_update = {
    "pokemon_id": "27006",
    "name": "Lilu12",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_add_pokeball = {
    "pokemon_id": "27006"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

