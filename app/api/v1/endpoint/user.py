from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.schema.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user_by_ci
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_new_usuario(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/{usuario_ci}", response_model=UserResponse)
def read_user(usuario_ci: str, db: Session = Depends(get_db)):
    db_usuario = get_user_by_ci(db, usuario_ci)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario
