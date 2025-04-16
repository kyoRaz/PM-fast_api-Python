from pydantic import BaseModel, EmailStr
from uuid import UUID
from app.users.models import User
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserOut(UserCreate):
    id: UUID
    is_active: bool

class UserUpdate(BaseModel):
    password: Optional[str] =None
    name: Optional[str] =None
    email:  Optional[EmailStr] =None
    is_active: Optional[bool] =None

