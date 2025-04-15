from fastapi import APIRouter
from app.users.models import User
from fastapi.responses import JSONResponse
from app.users.controller import create_user, get_user
from app.users.schema import UserCreate ,UserOut

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut, status_code=201)
def create_user_endpoint(user: UserCreate):
    return create_user(user)


@router.get("/{user_id}" , response_model=UserOut)
def route_get_user(user_id: int):
    return get_user(user_id)
