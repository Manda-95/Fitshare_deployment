from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_db
from models import User
from schemas import UserResponse, UserCreate
from auth.utils import get_password_hash, get_current_user
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/me", response_model=User)
async def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user

