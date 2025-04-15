from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parents[1] / ".env"
# print(env_path)
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"
# print(f"DATABASE_URL: {DATABASE_URL}")
# print(f"SECRET_KEY: {SECRET_KEY}")
# print(f"DEBUG: {DEBUG}")
