from fastapi import HTTPException, Path
from typing import Union
from app.models.pokemon import Pokemon
from app.services.pokemon_service import get_pokemon_data
import math

pokemons_list, list_pokemons = get_pokemon_data()

def get_total_pokemons() -> dict:
    return {"total": len(list_pokemons)}

def get_all_pokemons1() -> list[Pokemon]:
    return [Pokemon(**list_pokemons[id]) for id in list_pokemons]

def get_pokemon_by_id(id: int) -> Pokemon:
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    return Pokemon(**list_pokemons[id])

def create_pokemon(pokemon: Pokemon) -> Pokemon:
    if pokemon.id in list_pokemons:
        raise HTTPException(status_code=400, detail=f"Le pokemon {pokemon.id} existe d\u00e9j\u00e0 !")
    list_pokemons[pokemon.id] = pokemon.__dict__
    return pokemon

def update_pokemon(pokemon: Pokemon, id: int) -> Pokemon:
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail=f"Le pokemon {id} n'existe pas.")
    list_pokemons[id] = pokemon.__dict__
    return pokemon

def delete_pokemon(id: int) -> Pokemon:
    if id in list_pokemons:
        pokemon = Pokemon(**list_pokemons[id])
        del list_pokemons[id]
        return pokemon
    raise HTTPException(status_code=404, detail=f"Le pokemon {id} n'existe pas.")

def get_all_types() -> list[str]:
    types = []
    for pokemon in pokemons_list:
        for type_ in pokemon["types"]:
            if type_ not in types:
                types.append(type_)
    types.sort()
    return types

def search_pokemons(
    types: Union[str, None] = None,
    evo: Union[str, None] = None,
    totalgt: Union[int, None] = None,
    totallt: Union[int, None] = None,
    sortby: Union[str, None] = None,
    order: Union[str, None] = None,
) -> Union[list[Pokemon], None]:
    filtered_list = []

    if types is not None:
        for pokemon in pokemons_list:
            if set(types.split(",")).issubset(pokemon["types"]):
                filtered_list.append(pokemon)

    if evo is not None:
        tmp = filtered_list if filtered_list else pokemons_list
        new = []
        for pokemon in tmp:
            has_evo = "evolution_id" in pokemon
            if (evo == "true" and has_evo) or (evo == "false" and not has_evo):
                new.append(pokemon)
        filtered_list = new

    if totalgt is not None:
        tmp = filtered_list if filtered_list else pokemons_list
        filtered_list = [pokemon for pokemon in tmp if pokemon["total"] > totalgt]

    if totallt is not None:
        tmp = filtered_list if filtered_list else pokemons_list
        filtered_list = [pokemon for pokemon in tmp if pokemon["total"] < totallt]

    if sortby is not None and sortby in ["id", "name", "total"]:
        filtered_list = filtered_list if filtered_list else pokemons_list
        reverse = order == "desc"
        filtered_list = sorted(filtered_list, key=lambda d: d[sortby], reverse=reverse)

    if filtered_list:
        return [Pokemon(**pokemon) for pokemon in filtered_list]

    raise HTTPException(status_code=404, detail="Aucun Pokemon ne r\u00e9pond aux crit\u00e8res de recherche")

def get_all_pokemons_paginated(page: int = 1, items: int = 10) -> list[Pokemon]:
    items = min(items, 20)
    max_page = math.ceil(len(list_pokemons) / items)
    current_page = min(page, max_page)
    start = (current_page - 1) * items
    stop = start + items if start + items <= len(list_pokemons) else len(list_pokemons)
    sublist = list(list_pokemons)[start:stop]
    return [Pokemon(**list_pokemons[id]) for id in sublist]
