#Connecting to an API using python
#Author : Sriniketh M
#Date: 09-20-2025

import requests

url_base = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name): #name -> parameter
    url = f"{url_base}pokemon/{name}"
    response = requests.get(url) #response object gives a status code (HTTP) | 200 = response is okay or successful
    #print(response)

    #response is in JSON format
    if response.status_code == 200:
        pokemon_data = response.json() #this will convert to a dict
        return pokemon_data
    else:
        print(f"Failed to get data. Status code is {response.status_code}")

pokemon_name = "pikachu" #pokemon_name -> argument

pokemon_info = get_pokemon_info(pokemon_name) #parameters can be named different from the arguements

if pokemon_info:
    print(f"Pokemon name is {pokemon_info['name']}")
    print(f"Pokemon experience is {pokemon_info['base_experience']}")