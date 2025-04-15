from fastapi import HTTPException
from app.users.models import User
from app.users.schema import UserCreate

# Simuler une base en mémoire
users_db = {}

def create_user(user: UserCreate) -> User:
    user_id = len(users_db) + 1
    new_user = User(id=user_id,**user.dict())
    users_db[new_user.id] = new_user
    return new_user

def get_user(user_id: int) -> User:
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouv\u00e9.")
    return user
