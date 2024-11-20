from typing import Union
from datetime import datetime, timedelta, timezone
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, select
import jwt
from database import create_db_and_tables, get_db
from auth.routes import router as auth_router
from users.routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from category.routes import router as category_router
from exercises.routes import router as exercises_router

SECRET_KEY = "2e6f99cc653bd5ba9117e5e24d76bbc6b7b190681b5f90769ebaf8e5905f9526"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(category_router, prefix="/category", tags=["Category"])
app.include_router(exercises_router, prefix="/exercises", tags=["Exercise"])

