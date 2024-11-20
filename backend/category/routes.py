from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from database import get_db
from fastapi import APIRouter, Depends
from category.schemas import CategoryResponse, CategoryCreate
from models import Category

router = APIRouter()

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
