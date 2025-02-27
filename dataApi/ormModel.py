from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,DateTime
from dataApi.databaseConnection import engine 
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "Login_Activity"
    User_Name = Column(String(100), primary_key=True, index=True)
    Login_Time = Column(DateTime, nullable=False)
    Logout_Time = Column(DateTime, nullable=True)
    

Base.metadata.create_all(bind=engine)  # Ensure table exists