import uuid
from typing import Optional
from sqlmodel import SQLModel, Field
from uuid import UUID

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    password: Optional[str] = None
    is_active: bool = True
