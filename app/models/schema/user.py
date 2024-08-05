# app/models/schema/persona.py

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    last_name: str
    ci: str
    cellphone: str
    direction: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
