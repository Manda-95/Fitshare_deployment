from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from database import get_db
from fastapi import APIRouter, Depends
from goal.schemas import GoalResponse, GoalCreate
from models import Goal

router = APIRouter()

@router.post("/", response_model=GoalResponse, status_code=status.HTTP_201_CREATED)
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    db_goal = Goal(name=goal.name)
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

@router.get("/", response_model=list[GoalResponse])
def get_goals(db: Session = Depends(get_db)):
    return db.query(Goal).all()

