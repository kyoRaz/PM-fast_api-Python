from fastapi import APIRouter, Path
from app.pokemons.models import Pokemon
from app.pokemons.controller import (
    get_total_pokemons,
    get_all_pokemons1,
    get_pokemon_by_id,
    create_pokemon,
    update_pokemon,
    delete_pokemon,
    get_all_types,
    search_pokemons,
    get_all_pokemons_paginated
)

router = APIRouter(prefix="/pokemons", tags=["Pokemons"])

@router.get("/total")
def route_total():
    return get_total_pokemons()

@router.get("/")
def route_all_pokemons():
    return get_all_pokemons1()

@router.get("/{id}")
def route_get_by_id(id: int = Path(ge=1)):
    return get_pokemon_by_id(id)

@router.post("/")
def route_create(pokemon: Pokemon):
    return create_pokemon(pokemon)

@router.put("/{id}")
def route_update(pokemon: Pokemon, id: int = Path(ge=1)):
    return update_pokemon(pokemon, id)

@router.delete("/{id}")
def route_delete(id: int = Path(ge=1)):
    return delete_pokemon(id)

@router.get("/types/all")
def route_types():
    return get_all_types()

@router.get("/search")
def route_search(
    types: str | None = None,
    evo: str | None = None,
    totalgt: int | None = None,
    totallt: int | None = None,
    sortby: str | None = None,
    order: str | None = None
):
    return search_pokemons(types, evo, totalgt, totallt, sortby, order)

@router.get("/page")
def route_paginated(page: int = 1, items: int = 10):
    return get_all_pokemons_paginated(page, items)