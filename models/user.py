# imports for the object we extend from and the defining objects
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from config.setup import Base 

# extends
class Users(Base):
    # names the table in MYSQL
    __tablename__ = "users"

    # defines its columns 
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50),nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    # checks if email is formated correctly
    @validates("email")
    def validate_email(self, email):
        if "@" not in email and ".":
            raise ValueError("Invalid email")
        return email
    
    # TODO validate password is 8 characters and than encrypt

