# app/models/schema/persona.py

from pydantic import BaseModel


# se crea el Schema (el tipo de dato) para un usuario
class UserBase(BaseModel):
    name: str
    last_name: str
    ci: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
