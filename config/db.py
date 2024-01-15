from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sqlite.db")
Session = sessionmaker(bind=engine)
session = Session()