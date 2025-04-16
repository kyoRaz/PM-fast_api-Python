from sqlmodel import select, Session
from app.models.userModels import User
from uuid import UUID


def create_user(user: User, session: Session):
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        raise RuntimeError("Échec de la création de l'utilisateur.")


def get_all_users(session: Session):
    try:
        return session.exec(select(User)).all()
    except Exception:
        raise RuntimeError("Échec de la récupération des utilisateurs.")


def get_user_by_id(user_id: UUID, session: Session) -> User:
    try:
        user = session.get(User, user_id)
        if not user:
            raise ValueError("Utilisateur non trouvé.")
        return user
    except Exception as e:
        raise RuntimeError("Erreur interne lors de la récupération de l'utilisateur.")


def update_user(user_id: UUID, updated_data: dict, session: Session) -> User | None:
    try:
        user = session.get(User, user_id)
        if not user:
            return None

        for key, value in updated_data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        raise RuntimeError("Erreur interne lors de la mise à jour de l'utilisateur.")


def delete_user(user_id: UUID, session: Session) -> bool:
    try:
        user = session.get(User, user_id)
        if not user:
            return None

        session.delete(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        raise RuntimeError("Erreur lors de la suppression de l'utilisateur.")
