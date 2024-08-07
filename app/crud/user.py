# MecanicaMs/app/crud/user.py
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models.domain.user import User
from app.models.schema.user import UserCreate, UserResponseMessage


def create_user(db: Session, usuario: UserCreate) -> UserResponseMessage:
    db_usuario = User(
        ci=usuario.ci,
        name=usuario.name,
        last_name=usuario.last_name,
        cellphone=usuario.cellphone,
        direction=usuario.direction,
        auth_token=usuario.auth_token

    )
    try:
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return UserResponseMessage(detail="Usuario creado")
    except IntegrityError as ie:
        db.rollback()
        return None


def get_user_by_ci(db: Session, user_ci: str):
    return db.query(User).filter(user_ci == User.ci).first()


def get_user_by_token(db: Session, auth_token: str):
    return db.query(User).filter(auth_token == User.auth_token).first()
