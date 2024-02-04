from fastapi import FastAPI, HTTPException
from dataclasses import dataclass
from typing import Union
import json
import math

#===== Structure de données : Dictionnaire indexé par pokemon id =====#
with open("pokemons.json", "r") as f:
    pokemons_list = json.load(f)

list_pokemons = {k+1:v for k, v in enumerate(pokemons_list)}
#======================================================================
@dataclass
class Pokemon() :
    id: int
    name: str
    types: list[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: Union[int, None] = None

app = FastAPI()

@app.get("/pokemons/", response_model=list[Pokemon])
def get_all_pokemons(page: int=1, items: int=10) -> list[Pokemon]:

    items = min(items, 20)
    max_page = math.ceil(len(list_pokemons) / items)
    current_page = min(page, max_page)
    start = (current_page-1)*items + 1
    stop = start + items if start + items <= len(list_pokemons) + 1 else len(list_pokemons) + 1

    res = []

    for id in range(start, stop) :
        print(id)
        res.append(Pokemon(**list_pokemons[id]))
    
    return res

@app.get("/pokemon/{id}", response_model=Pokemon)
def get_pokemon_by_id(id: int) -> Pokemon :

    if id < 1 or id > len(pokemons_list) :
        raise HTTPException(status_code=404, detail="Pokemon inconnu")
    
    return Pokemon(**list_pokemons[id])

@app.get("/types")
def get_all_types()->list[str]:

    types = []
    for pokemon in pokemons_list :
        for type in pokemon["types"] :
            if type not in types :
                types.append(type)
    types.sort()
    return types


@app.get("/pokemons/search/", response_model=list[Pokemon])
def search_pokemons(
    types: Union[str, None] = None,
    evo : Union[str, None] = None
)->Union[list[Pokemon], None] :
    
    filtered_list = []
    res = []

    #On filtre les types
    if types is not None :
        for pokemon in pokemons_list :
            if set(types.split(",")).issubset(pokemon["types"]) :
                filtered_list.append(pokemon)

    #On filtre les evolutions
    if evo is not None :
        tmp = filtered_list if filtered_list else pokemons_list
        new = []
        
        for pokemon in tmp :
            if evo == "true" and "evolution_id" in pokemon:
                new.append(pokemon)
            if evo == "false" and "evolution_id" not in pokemon:
                new.append(pokemon)
        filtered_list = new
        
    #Réponse           
    if filtered_list :
        for pokemon in filtered_list :
            res.append(Pokemon(**pokemon))
        return res
    
    raise HTTPException(status_code=404, detail="Aucun Pokemon ne répond aux critères de recherche")
