from fastapi import APIRouter ,Depends
from sqlmodel import Session
from typing import List
from uuid import UUID
from app.core.database import get_session
from app.users.schema import UserCreate ,UserOut
from app.users.controller import createUser, getUser ,getAllUser


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut, status_code=201)
def create_user_endpoint(user: UserCreate,session: Session = Depends(get_session)):
    return createUser(user,session)


@router.get("/{user_id}" , response_model=UserOut)
def route_get_user(user_id : UUID, session: Session = Depends(get_session)):
    return getUser(user_id , session)


@router.get("/" , response_model=List[UserOut])
def route_get_all_user(session: Session = Depends(get_session)):
    return getAllUser(session)
