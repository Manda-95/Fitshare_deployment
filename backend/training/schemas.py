from pydantic import BaseModel
from typing import List


class TrainingCreate(BaseModel):
    title: str 
    theme: str 
    goal: str
    difficulty: str 
    exercises: List[dict]



class TrainingResponse(BaseModel):
    title: str 
    theme: str 
    goal: str
    difficulty: str 
    exercises: str



