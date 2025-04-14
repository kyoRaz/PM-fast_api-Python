from fastapi import FastAPI
from app.pokemons.router import router as pokemon_router
from app.users.router import router as user_router
from app.departments.router import router as department_router

app = FastAPI()

app.include_router(pokemon_router)
app.include_router(user_router)
app.include_router(department_router)
