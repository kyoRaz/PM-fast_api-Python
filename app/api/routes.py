from fastapi import APIRouter, Path
from app.models.pokemon import Pokemon
from app.controllers.pokemon_controller import *

router = APIRouter()

@router.get("/total_pokemons")
def route_total():
    return get_total_pokemons()

@router.get("/pokemons")
def route_all_pokemons():
    return get_all_pokemons1()

@router.get("/pokemon/{id}")
def route_get_by_id(id: int = Path(ge=1)):
    return get_pokemon_by_id(id)

@router.post("/pokemon/")
def route_create(pokemon: Pokemon):
    return create_pokemon(pokemon)

@router.put("/pokemon/{id}")
def route_update(pokemon: Pokemon, id: int = Path(ge=1)):
    return update_pokemon(pokemon, id)

@router.delete("/pokemon/{id}")
def route_delete(id: int = Path(ge=1)):
    return delete_pokemon(id)

@router.get("/types")
def route_types():
    return get_all_types()

@router.get("/pokemons/search/")
def route_search(**kwargs):
    return search_pokemons(**kwargs)

@router.get("/pokemons2/")
def route_paginated(page: int = 1, items: int = 10):
    return get_all_pokemons_paginated(page, items)
