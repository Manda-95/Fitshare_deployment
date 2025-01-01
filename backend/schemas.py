from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

class CreatorResponse(BaseModel):
    id: int
    username: str
    email: Optional[str]

    class Config:
        orm_mode = True
        
# Training
class TrainingCreate(BaseModel):
    title: str
    description: str
    category_id: int
    goal_id: int
    difficulty: str
    exercises: List[int]  # Liste d'IDs d'exercices

class TrainingResponse(BaseModel):
    id: int
    title: str 
    description: str
    category: str
    goal: str
    difficulty: str 
    exercises: List["ExerciseResponse"]
    creator: Optional[CreatorResponse] 
    comments: List["CommentResponse"]

    class Config:
        orm_mode = True

# Use
class UserResponse(BaseModel):
    username: str
    email: str | None = None
    trainings: List[TrainingResponse] = []


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ExerciseCreate(BaseModel):
    name: str
    id_category: int

class ExerciseResponse(BaseModel):
    id: int
    name: str
    id_category: int

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    content: str
    training_id: int

class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    training_id: int
    author: Optional["UserResponse"]  # Inclure les informations de l'auteur

    class Config:
        orm_mode = True


class EventCreate(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    training_id: Optional[int] = None
    description: Optional[str] = None

class EventResponse(BaseModel):
    id: int
    title: str
    start_time: datetime
    end_time: datetime
    training_id: Optional[int]
    description: Optional[str]

    class Config:
        orm_mode = True