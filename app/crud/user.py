# MecanicaMs/app/crud/user.py
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models.domain.user import User
from app.models.schema.user import UserCreate


def create_user(db: Session, usuario: UserCreate):
    db_usuario = User(
        ci=usuario.ci,
        name=usuario.name,
        last_name=usuario.last_name,
        cellphone=usuario.cellphone,
        direction=usuario.direction

    )
    try:
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return {"detail": "Vehiculo creado"}
    except IntegrityError as ie:
        db.rollback()
        return None


def get_user_by_ci(db: Session, user_ci: str):
    return db.query(User).filter(user_ci == User.ci).first()
