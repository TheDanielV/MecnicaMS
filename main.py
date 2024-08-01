# app/main.py

from fastapi import FastAPI
from app.api.v1.endpoint import user
from app.db.init_db import init_db

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["user"])


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}
