from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from database import get_db
from fastapi import APIRouter, Depends
from training.schemas import TrainingResponse, TrainingCreate
from models import Training
import json

router = APIRouter()

@router.post("/", response_model=TrainingResponse, status_code=status.HTTP_201_CREATED)
def create_training(training: TrainingCreate, db: Session = Depends(get_db)):
    db_training = Training(
        title=training.title,
        theme=training.theme,
        goal=training.goal,
        difficulty=training.difficulty,
        exercises=json.dumps(training.exercises), 
    )
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training

