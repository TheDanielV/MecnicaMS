# app/models/domain/persona.py

from sqlalchemy import Column, Integer, String
from app.db.database import Base


# Se crea el modelo paara un usuario
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    ci = Column(String(100), unique=True, index=True)
    name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    cellphone = Column(String(100), index=True)
    direction = Column(String(100), index=True)
    auth_token = Column(String(100), index=True)

