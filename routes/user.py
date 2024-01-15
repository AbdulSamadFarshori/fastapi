from fastapi import APIRouter
from config.db import session
from model.user import Users
from schemas.user import User
from typing import Union, List, Dict


user = APIRouter()


@user.get("/")
async def get_all_users():
    query = session.query(Users)
    all_data = query.all()
    return all_data


@user.get("/{id}")
async def get_users(id: int):
    query = session.query(Users)
    filter_data = query.filter(Users.id == id)
    return filter_data.all()

@user.post("/add-user")
async def add_users(user:User):
    print(user)
    data = Users(name=user.name, email=user.email, password=user.password)
    session.add(data)
    session.commit()
    data = session.query(Users).all()
    return data[-1] 