from fastapi import HTTPException
from app.users.models import User

# Simuler une base en mémoire
users_db = {}

def create_user(user: User) -> User:
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="L'utilisateur existe d\u00e9j\u00e0.")
    users_db[user.id] = user
    return user

def get_user(user_id: int) -> User:
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouv\u00e9.")
    return user
