import requests

def get_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    response = requests.get(url)

    if response.status_code == 200:
        tipo_cambio = response.json()
        return tipo_cambio
    else:
        print("Error al obtener el tipo de cambio")
        return None


def get_pokedex_data():
    url = "https://pokeapi.co/api/v2/pokedex/1/"
    response = requests.get(url)

    if response.status_code == 200:
        pokedex_data = response.json()
        return pokedex_data
    else:
        print("Error al obtener los datos de la Pokédex")
        return None


def get_pokemon_data(name):
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(name)
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Error al obtener los datos del Pokémon")
        return None