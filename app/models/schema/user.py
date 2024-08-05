# app/models/schema/persona.py

from pydantic import BaseModel


class UserBase(BaseModel):
    ci: str
    name: str
    last_name: str
    cellphone: str
    direction: str
    auth_token: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserResponseMessage(BaseModel):
    detail: str
