import requests
import pandas as pd
import time

url_base = "https://pokeapi.co/api/v2/"

pokemon_df = pd.read_csv("pokemon.csv")

species_ids = pokemon_df['species_id'].dropna().unique()

def get_pokemon_species_info(species_id):

    url = f"{url_base}pokemon-species/{species_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        species_info = response.json()
        return species_info
    
    except requests.exceptions.RequestException as e:
        print("Response failed to fetch species info: {e}")

species_rows = []        

species_ids_5 = species_ids[385:395]

for i, id_species in enumerate(species_ids_5, start = 1):

    try:
        time.sleep(0.2)
        species_info = get_pokemon_species_info(id_species)

        print(f"Getting species {i} of {len(species_ids_5)}: {species_info['name']}")

        species_rows.append(
            {
                "species_id": species_info.get('id'),
                "name": species_info.get('name'),
                "color": species_info.get('color').get('name'),
                #"habitat": species_info.get('habitat' or {}).get('name'), #if habitat is empty, then an empty dict. O/P is None
                "legendary_status": species_info['is_legendary'],
                'mythical_status': species_info['is_mythical']
            }
        )

    except requests.exceptions.RequestException as e:
        print(f"Network error fetching {id_species}: {e}")
    except KeyError as e:
        print(f"Missing key {e} in {id_species}")
    except Exception as e:
        print(f"Unexpected error with {id_species}: {e}")

species_df = pd.DataFrame(species_rows)

species_df.to_csv("species.csv", index = False)