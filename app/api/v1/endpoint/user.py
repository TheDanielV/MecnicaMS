from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.schema.user import UserCreate, UserResponse, UserResponseMessage
from app.crud.user import create_user, get_user_by_ci, get_user_by_token
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=UserResponseMessage)
def create_new_usuario(user: UserCreate, db: Session = Depends(get_db)):
    result = create_user(db, user)
    if result is None:
        raise HTTPException(status_code=422, detail="El usuario ya existe")
    return result


@router.get("/{usuario_ci}", response_model=UserResponse)
def read_user(usuario_ci: str, db: Session = Depends(get_db)):
    db_usuario = get_user_by_ci(db, usuario_ci)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario


@router.get("/user_token/{user_token}", response_model=UserResponse)
def read_user_by_token(user_token: str, db: Session = Depends(get_db)):
    db_usuario = get_user_by_token(db, user_token)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario
