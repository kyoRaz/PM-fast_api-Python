from fastapi import APIRouter
from app.users.models import User
from app.users.controller import create_user, get_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def route_create_user(user: User):
    return create_user(user)

@router.get("/{user_id}")
def route_get_user(user_id: int):
    return get_user(user_id)
