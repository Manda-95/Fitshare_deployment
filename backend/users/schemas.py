from pydantic import BaseModel

class UserResponse(BaseModel):
    username: str
    email: str | None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
