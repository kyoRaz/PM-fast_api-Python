import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "pokemons.json"

with open(DATA_PATH, "r") as f:
    pokemons_list = json.load(f)

list_pokemons = {k+1: v for k, v in enumerate(pokemons_list)}

def get_pokemon_data():
    return pokemons_list, list_pokemons
