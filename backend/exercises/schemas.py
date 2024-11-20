from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    name: str
    id_category: int

class ExerciseResponse(BaseModel):
    name: str
    id_category: int
