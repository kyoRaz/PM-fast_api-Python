from sqlmodel import select , Session
from app.core.database import get_session
from app.users.models import User
from uuid import UUID


def create_user(user: User, session = Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_all_users(session = Session):
    return session.exec(select(User)).all()

def get_user_by_id(user_id: UUID, session = Session ) -> User | None:
    return session.get(User, user_id)


def updateser(user_id: UUID, updated_data: dict, session = Session ) -> User | None:
    user = session.get(User, user_id)
    if not user:
        return None

    for key, value in updated_data.items():
        setattr(user, key, value)

    session.add(user)  
    session.commit()
    session.refresh(user)
    return user