from fastapi import FastAPI
from app.api.routes import router as pokemon_router

app = FastAPI()

app.include_router(pokemon_router)
