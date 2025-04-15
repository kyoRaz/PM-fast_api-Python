from fastapi import HTTPException
from app.users.models import User
from app.users.schema import UserCreate 
from app.users.service import create_user ,get_all_users
from sqlmodel import Session
from typing import List

# Simuler une base en mémoire
users_db = {}

def createUser(user: UserCreate,session: Session ) -> User:
    new_user = User(**user.dict())
    create_user(new_user,session)
    return new_user

def getUser(user_id: int) -> User:
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouv\u00e9.")
    return user

def getAllUser(session: Session ) -> List[User]:
    return get_all_users(session)
