from fastapi import FastAPI
from app.pokemons.router import router as pokemon_router
from app.users.router import router as user_router
from app.departments.router import router as department_router
from dotenv import load_dotenv
import os
from pathlib import Path
import asyncio
import uvicorn

# === Chargement des variables d'environnement ===
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# DATABASE_URL = os.getenv("DATABASE_URL")
# SECRET_KEY = os.getenv("SECRET_KEY")
# DEBUG = os.getenv("DEBUG", "False") == "True"

# print(f"DATABASE_URL: {DATABASE_URL}")
# print(f"DEBUG: {DEBUG}")

# === Création de l'app FastAPI ===
app = FastAPI()

app.include_router(pokemon_router)
app.include_router(user_router)
app.include_router(department_router)

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
