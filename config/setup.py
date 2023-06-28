from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "mysql+mysqlconnector://root:nerd@localhost/media_db"
engine = create_engine(db_url)
base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Users(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255),nullable=False)

base.metadata.create_all(engine)
