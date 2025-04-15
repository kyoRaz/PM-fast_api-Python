from sqlmodel import select
from app.core.database import get_session
from app.users.models import User
from fastapi import Depends

def get_all_users(session = Depends(get_session)):
    return session.exec(select(User)).all()

def create_user(user: User, session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user