from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel
from typing import Optional, List


app = FastAPI(title="My first app")

engine = create_engine("sqlite:///users.db", connect_args={"check_same_thread":"Fasle"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    role = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)


Base.metadata.create_all(engine)

#Pydentic Models (Dataclass)
class UserCreate(BaseModel):
    name:str
    email:str
    role:str

class UserResponce(BaseModel):
    id:int
    name:str
    email:str
    role:str

    class Config:
        from_attributes = True;

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()

@app.get("/")
def root():
    return {"message":"Hi there!!!"}



