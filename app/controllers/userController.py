from fastapi import HTTPException
from app.models.userModels import User
from app.schemas.schema import UserCreate, UserUpdate
import app.services.userService as userService
from sqlmodel import Session
from typing import List
from uuid import UUID
from fastapi.responses import JSONResponse


def createUser(user: UserCreate, session: Session) -> User:
    try:
        new_user = User(**user.model_dump())
        userService.create_user(new_user, session)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors de la création de l'utilisateur.")


def getUser(user_id: UUID, session: Session) -> User:
    try:
        return userService.get_user_by_id(user_id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération de l'utilisateur.")


def getAllUser(session: Session) -> List[User]:
    try:
        return userService.get_all_users(session)
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération des utilisateurs.")


def updateUser(user_id: UUID, updated_data: UserUpdate, session: Session) -> User:
    try:
        updated_data = dict(updated_data)
        user = userService.update_user(user_id, updated_data, session)
        if not user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé pour mise à jour.")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors de la mise à jour de l'utilisateur.")


def patchUser(user_id: UUID, updated_data: UserUpdate, session: Session) -> User:
    try:
        updated_data = updated_data.model_dump(exclude_unset=True)
        user = userService.update_user(user_id, updated_data, session)
        if not user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé pour mise à jour partielle.")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors du patch de l'utilisateur.")


def deleteUser(user_id: UUID, session: Session):
    try:
        success = userService.delete_user(user_id, session)
        if not success:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé pour suppression.")
        return JSONResponse(
            status_code=200,
            content={"message": "Utilisateur supprimé avec succès", "user_id": str(user_id)}
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors de la suppression de l'utilisateur.")
