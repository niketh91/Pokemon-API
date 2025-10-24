# main.py
# Pokémon Data Engineering Pipeline
# Author: Sriniketh M

import os
from src.pokemoninfoapi import fetch_pokemon_info
from src.pokemonabilities import fetch_ability_data
from src.pokemonspecies import fetch_species_data

def main():
    print(f"Starting Pokemon Data Pipeline...\n")

    #Create data folder
    os.makedirs("data", exist_ok= True)

    #Fetch core pokemon info
    print(f"Fetching core pokemon info...\n")
    pokemon_info_data = fetch_pokemon_info(400)

    #Get the dict of dataframes from pokemoninfoapi.py file
    pokemon_df = pokemon_info_data["pokemon"]
    pokemon_ability_df = pokemon_info_data["pokemon_ability"]
    pokemon_type_df = pokemon_info_data["pokemon_type"]
    pokemon_stats_df = pokemon_info_data["pokemon_stats"]
    type_df = pokemon_info_data["type"]
                                
    print(f"Successfully fetched pokemon info!!")
    print(f"Count of pokemons {len(pokemon_df)}")
    print(f"Abilities fetched {len(pokemon_ability_df)}")
    
    #Get ability info
    print(f"Getting detailed ability info...\n")
    ability_df = fetch_ability_data(pokemon_ability_df)
    print(f"Gathered {len(ability_df)} ability records")

    #Get species info
    print(f"Getting detailed species info...\n")
    species_df = fetch_species_data(pokemon_df)
    print(f"Gathered {len(species_df)} species records")

    #Saving all dfs to csv
    print(f"Saving all info as CSV files in the data folder...\n")

    pokemon_df.to_csv("data/pokemon.csv", index= False)
    pokemon_ability_df.to_csv("data/pokemon_ability.csv", index= False)
    pokemon_type_df.to_csv("data/pokemon_type.csv", index= False)
    pokemon_stats_df.to_csv("data/pokemon_stats.csv", index= False)
    type_df.to_csv("data/type.csv", index= False)
    ability_df.to_csv("data/ability.csv", index= False)
    species_df.to_csv("data/species.csv", index= False)

    print(f"Data pipeline successfully completed. Files saved in data folder!")

if __name__ == "__main__":
    main()