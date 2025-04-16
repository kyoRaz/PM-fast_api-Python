from fastapi import APIRouter ,Depends
from sqlmodel import Session
from typing import List
from uuid import UUID
from app.core.database import get_session
from app.users.schema import UserCreate ,UserOut , UserUpdate
import app.users.controller as userCtrl


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut, status_code=201)
def create_user_endpoint(user: UserCreate,session: Session = Depends(get_session)):
    return userCtrl.createUser(user,session)


@router.get("/{user_id}" , response_model=UserOut)
def route_get_user(user_id : UUID, session: Session = Depends(get_session)):
    return userCtrl.getUser(user_id , session)


@router.get("/" , response_model=List[UserOut])
def route_get_all_user(session: Session = Depends(get_session)):
    return userCtrl.getAllUser(session)


@router.put("/{user_id}" , response_model=UserOut)
def route_update_user(user_id : UUID,updatedData : UserUpdate ,session: Session = Depends(get_session)):
    return userCtrl.updateUser(user_id ,updatedData, session)

@router.patch("/{user_id}" , response_model=UserOut)
def route_update_user(user_id : UUID,updatedData : UserUpdate ,session: Session = Depends(get_session)):
    return userCtrl.patchUser(user_id ,updatedData, session)
