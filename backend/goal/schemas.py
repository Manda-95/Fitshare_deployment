from pydantic import BaseModel

class GoalCreate(BaseModel):
    name: str

class GoalResponse(BaseModel):
    name: str