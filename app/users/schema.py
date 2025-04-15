from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserOut(UserCreate):
    id: int
    is_active: bool
