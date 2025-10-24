import pandas as pd
import requests
import time

url_base = "https://pokeapi.co/api/v2/"

def fetch_ability_data(pokemon_ability_df):
    ability_ids = pokemon_ability_df['ability_id'].dropna().unique()

    def get_pokemon_ability(ability_id):
        url = f"{url_base}ability/{ability_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            ability_info = response.json()
            return ability_info
        
        except requests.exceptions.RequestException as e:
            print(f"Response failed to fetch ability {ability_id} : {e}")
            return None

    pokemon_ability_rows = []

    for i, id_ability in enumerate(ability_ids, start=1):

        try:
            time.sleep(0.2)
            ability_info = get_pokemon_ability(id_ability)
            if not ability_info:
                continue

            print(f"Getting ability {i} of {len(ability_ids)}: {ability_info['name']}")
            effect_entries = ability_info['effect_entries']
            position_en = next((entry for entry in effect_entries if entry['language']['name'] == 'en'), None)
            #this gives the dictionary where the language is english

            pokemon_ability_rows.append(
                {
                    "ability_id": ability_info['id'],
                    "name": ability_info['name'],
                    'is_main_series': ability_info['is_main_series'],
                    "generation": ability_info['generation']['name'],
                    "short_effect": position_en['short_effect']
                }
            )

        except Exception as e:
            print(f"Unexpected error with {id_ability}: {e}")
            
    return pd.DataFrame(pokemon_ability_rows)

if __name__ == "__main__":
    df = fetch_ability_data()
    print(df.head())