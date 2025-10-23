#Connecting to Poke API using python
#Author : Sriniketh M
#Date: 09-20-2025

import requests

def get_pokemon_names(limit):

    url_base = "https://pokeapi.co/api/v2/"

    #limit = 100 #default is 20

    url = f"{url_base}pokemon/?limit={limit}"

    #First getting the list of all pokemon names. Should be 1302 in total
    pokemon_names = []
    page = 0

    while url:
        try:
            print(f"Getting data from page {page}. URL is {url}")
            response = requests.get(url)
            response.raise_for_status() #Raises HTTP error if any
            data = response.json()

            pokemon_list = data['results'] #this has names and url for each pokemon

            for pokemon in pokemon_list:
                poke = (pokemon['name'])
                pokemon_names.append(poke)

            url = data['next']
            page +=1
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed with error: {e}")

    return pokemon_names

# pokemon_name = "pikachu" #pokemon_name -> argument

# pokemon_info = get_pokemon_info(pokemon_name) #parameters can be named different from the arguements

# if pokemon_info:
#     print(f"Pokemon name is {pokemon_info['name']}")
#     print(f"Pokemon experience is {pokemon_info['base_experience']}")