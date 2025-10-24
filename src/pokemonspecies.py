import requests
import pandas as pd
import time

url_base = "https://pokeapi.co/api/v2/"

def fetch_species_data(pokemon_df):
    species_ids = pokemon_df['species_id'].dropna().unique()
            
    def get_pokemon_species_info(species_id):
        url = f"{url_base}pokemon-species/{species_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            species_info = response.json()
            return species_info
        
        except requests.exceptions.RequestException as e:
            print(f"Response failed to fetch species info: {e}")
            return None

    species_rows = []        

    for i, id_species in enumerate(species_ids, start = 1):

        try:
            time.sleep(0.2)
            species_info = get_pokemon_species_info(id_species)
            if not species_info:
                continue

            print(f"Getting species {i} of {len(species_ids)}: {species_info['name']}")

            species_rows.append(
                {
                    "species_id": species_info.get('id'),
                    "name": species_info.get('name'),
                    "color": species_info.get('color' or {}).get('name'),
                    "legendary_status": species_info['is_legendary'],
                    'mythical_status': species_info['is_mythical']
                }
            )

        except Exception as e:
            print(f"Unexpected error with {id_species}: {e}")

    return pd.DataFrame(species_rows)

if __name__ == "__main__":
    df = fetch_species_data()
    print(df.head())