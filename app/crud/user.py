# MecanicaMs/app/crud/user.py

from sqlalchemy.orm import Session
from app.models.domain.user import User
from app.models.schema.user import UserCreate

def create_user(db: Session, usuario: UserCreate):
    db_usuario = User(
        ci=usuario.ci,
        name=usuario.name,
        last_name=usuario.last_name
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_user_by_ci(db: Session, user_ci: str):
    return db.query(User).filter(User.ci == user_ci).first()
