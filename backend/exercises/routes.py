from fastapi import APIRouter, Depends, status
from sqlmodel import Field, Session, SQLModel, select
from database import get_db
from fastapi import APIRouter, Depends
from schemas import ExerciseResponse, ExerciseCreate
from models import Exercise

router = APIRouter()

@router.get("/category/{category_id}", response_model=list[ExerciseResponse])
def get_exercises_by_category(category_id: int, db: Session = Depends(get_db)):
    statement = select(Exercise).where(Exercise.id_category == category_id)
    results = db.exec(statement).all()
    return results

@router.post("/", response_model=ExerciseResponse, status_code=status.HTTP_201_CREATED)
def create_exercises(exercise: ExerciseCreate, db: Session = Depends(get_db)):
    db_exercise = Exercise(name=exercise.name, id_category=exercise.id_category)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise
