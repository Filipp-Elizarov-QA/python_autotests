import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN ='bc523580e6a93e6d8013f33b64e7fb78'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '4056'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_status_code():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Zaba123' 

@pytest.mark.parametrize('key, value',[('name','Zaba123'),('trainer_id', TRAINER_ID),('id','27011')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value