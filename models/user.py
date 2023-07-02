# imports for the object we extend from and the defining objects
from sqlalchemy import Column, Integer, String
from config.setup import Base 

# extends
class Users(Base):
    # names the table in MYSQL
    __tablename__ = "users"

    # defines its columns 
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255),nullable=False)
