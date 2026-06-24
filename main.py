from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel
from typing import Optional, List


app = FastAPI(title="My first app")

engine = create_engine("sqlite:///users.db")

@app.get("/")
def root():
    return {"message":"Hi there!!!"}



