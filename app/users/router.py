from fastapi import APIRouter ,Depends
from app.users.models import User
from fastapi.responses import JSONResponse
from app.users.controller import createUser, getUser
from app.users.schema import UserCreate ,UserOut
from app.core.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut, status_code=201)
def create_user_endpoint(user: UserCreate,session: Session = Depends(get_session)):
    return createUser(user,session)


@router.get("/{user_id}" , response_model=UserOut)
def route_get_user(user_id: int):
    return getUser(user_id)
