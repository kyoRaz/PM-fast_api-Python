from fastapi import HTTPException
from app.users.models import User
from app.users.schema import UserCreate , UserUpdate
import app.users.service as userService
from sqlmodel import Session
from typing import List
from uuid import UUID
from fastapi.responses import JSONResponse


# Simuler une base en mémoire
users_db = {}

def createUser(user: UserCreate,session: Session ) -> User:
    new_user = User(**user.dict())
    userService.create_user(new_user,session)
    return new_user

def getUser(user_id : UUID , session: Session) -> User:
    user = userService.get_user_by_id(user_id,session)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouv\u00e9.")
    return user

def getAllUser(session: Session ) -> List[User]:
    return userService.get_all_users(session)


def updateUser(user_id: UUID,updated_data:UserUpdate , session: Session ) -> List[User]:
    updated_data= dict(updated_data)
    return userService.update_user(user_id,updated_data,session)

def patchUser(user_id: UUID,updated_data:UserUpdate , session: Session ) -> List[User]:
    updated_data=updated_data.model_dump(exclude_unset=True)
    return userService.update_user(user_id,updated_data,session)

def deleteUser(user_id : UUID , session: Session) :
    user = userService.delete_user(user_id,session)
    if not user:
        raise HTTPException(status_code=500, detail="suppression echoué")
    return JSONResponse(
        status_code=200,
        content={"message": "Utilisateur supprimé avec succès", "user_id": str(user_id)}
    )