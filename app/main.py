from fastapi import FastAPI
from app.pokemons.router import router as pokemon_router
from app.users.router import router as user_router
from app.departments.router import router as department_router
from dotenv import load_dotenv
import os
from pathlib import Path
import asyncio
import uvicorn
from sqlmodel import SQLModel
from app.core.database import engine

# === Chargement des variables d'environnement ===
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# === BDD ===

def create_db():
    SQLModel.metadata.create_all(engine)
    print("table crées")


# === Création de l'app FastAPI ===
app = FastAPI()

app.include_router(pokemon_router)
app.include_router(user_router)
app.include_router(department_router)

# Initialisation de la base au démarrage
@app.on_event("startup")
def on_startup():
    create_db()

# === Fonction de lancement propre avec gestion d'erreurs ===
async def start():
    config = uvicorn.Config("main:app", host="127.0.0.1", port=8000, reload=True)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    try:
        asyncio.run(start())
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("🛑 Serveur interrompu proprement.")
