from pokemonapi import get_pokemon_names
import pandas as pd
import requests
import time

pokemon_names = get_pokemon_names(400)

print(f"Saved {len(pokemon_names)} pokemons to the list!")

url_base = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name): #name -> parameter
    url = f"{url_base}pokemon/{name}"
    
    try:
        response = requests.get(url) 
        response.raise_for_status() #Raises HTTP error if any occurs
        
    #response is in JSON format
        pokemon_data = response.json() #this will convert to a dict
        return pokemon_data
    
    except requests.exceptions.RequestException as e:
        print(f"Response Failed : {e}")

pokemon_rows = []
pokemon_ability_rows = []
pokemon_type_rows = []
pokemon_stat_rows = []
type_rows = []

for poke_index, pokemon_name in enumerate(pokemon_names):

    try:
        time.sleep(0.2)  # Small delay to avoid hitting rate limits
        pokemon_info = get_pokemon_info(pokemon_name)
        print(f"Getting info about pokemon {poke_index+1} from the list - {pokemon_info['name']}")

        species = pokemon_info['species']['url']
        pokemon_rows.append(
            {
                "pokemon_id": pokemon_info['id'],
                "name": pokemon_info['name'],
                "is_default": pokemon_info['is_default'],
                "height": pokemon_info['height'],
                "weight": pokemon_info['weight'],
                "base_experience": pokemon_info['base_experience'],
                "species_id": species.strip("/").split("/")[-1],
            }
        )

        for ability in pokemon_info['abilities']:
            pokemon_ability_rows.append(
                {
                    "pokemon_id": pokemon_info['id'],
                    "ability_id": ability['ability']['url'].strip("/").split("/")[-1],
                    "ability_hidden": ability['is_hidden'],
                    "slot": ability['slot']
                }
            )
        
        for ptype in pokemon_info['types']:
            type_id = ptype['type']['url'].strip("/").split("/")[-1]
            
            pokemon_type_rows.append(
                {
                    "pokemon_id": pokemon_info['id'],
                    "type_id":type_id,
                    "slot": ptype['slot']
                }
            )

            type_rows.append(
                {
                    "type_id": type_id,
                    "name": ptype['type']['name']
                }
            )

        for stat in pokemon_info['stats']:
            pokemon_stat_rows.append(
                {
                    "pokemon_id": pokemon_info['id'],
                    "stat_name": stat['stat']['name'],
                    "base_stat": stat['base_stat'],
                    "effort": stat['effort']
                }
            )

    except requests.exceptions.RequestException as e:
        print(f"Network error fetching {pokemon_name}: {e}")
    except KeyError as e:
        print(f"Missing key {e} in {pokemon_name}")
    except Exception as e:
        print(f"Unexpected error with {pokemon_name}: {e}")

pokemon_df = pd.DataFrame(pokemon_rows)
pokemon_ability_df = pd.DataFrame(pokemon_ability_rows)
pokemon_type_df = pd.DataFrame(pokemon_type_rows)
pokemon_stat_df = pd.DataFrame(pokemon_stat_rows)
type_df = pd.DataFrame(type_rows).drop_duplicates().reset_index(drop=True)

pokemon_df.to_csv("pokemon.csv", index = False)
pokemon_ability_df.to_csv("pokemon_ability.csv", index = False)
pokemon_type_df.to_csv("pokemon_type.csv", index = False)
pokemon_stat_df.to_csv("pokemon_stat.csv", index = False)
type_df.to_csv("type.csv", index = False)