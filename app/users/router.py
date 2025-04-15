from fastapi import APIRouter
from app.users.models import User
from app.users.controller import create_user, get_user
from app.users.schema import UserCreate ,UserOut

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def route_create_user(user: UserCreate):
    return create_user(user)

@router.get("/{user_id}" , response_model=UserOut)
def route_get_user(user_id: int):
    return get_user(user_id)
