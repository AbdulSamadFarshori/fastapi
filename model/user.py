from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import declarative_base
from config.db import engine
Base =  declarative_base()

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))

Base.metadata.create_all(engine)
