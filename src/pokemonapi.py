import requests

def fetch_pokemon_names(limit=400):

    url_base = "https://pokeapi.co/api/v2/"

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

            for pokemon in data['results']:
                pokemon_names.append(pokemon['name'])

            url = data['next']
            page +=1
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed with error: {e}")
            break

    print(f"Retrieved {len(pokemon_names)} Pokémon names.")
    return pokemon_names

if __name__ == "__main__":
    # Optional: run this file alone for testing
    fetch_pokemon_names(50)