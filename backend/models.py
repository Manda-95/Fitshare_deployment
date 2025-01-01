from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class TrainingExerciseLink(SQLModel, table=True):
    training_id: int = Field(foreign_key="training.id", primary_key=True)
    exercise_id: int = Field(foreign_key="exercise.id", primary_key=True)

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    trainings: List["Training"] = Relationship(back_populates="creator")
    comments: List["Comment"] = Relationship(back_populates="author")  
    events: list["Event"] = Relationship(back_populates="user")

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=False, nullable=False)
    trainings: List["Training"] = Relationship(back_populates="category")

class Exercise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=False, nullable=False)
    id_category: int = Field(foreign_key="category.id", nullable=False)
    trainings: List["Training"] = Relationship(back_populates="exercises", link_model=TrainingExerciseLink)

class Goal(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=False, nullable=False)
    trainings: List["Training"] = Relationship(back_populates="goal")

class Training(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True, unique=False, nullable=False)
    difficulty: str = Field(index=True, unique=False, nullable=False)
    description: str = Field(index=True, unique=False, nullable=False)
    category: Optional[Category] = Relationship(back_populates="trainings")
    category_id: int = Field(foreign_key="category.id", nullable=False)
    goal_id: int = Field(foreign_key="goal.id", nullable=False)
    goal: Optional[Goal] = Relationship(back_populates="trainings")
    exercises: List[Exercise] = Relationship(back_populates="trainings", link_model=TrainingExerciseLink)
    creator_id: int = Field(foreign_key="user.id", nullable=False)
    creator: Optional["User"] = Relationship(back_populates="trainings")
    comments: List["Comment"] = Relationship(back_populates="training")

class Comment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    training_id: int = Field(foreign_key="training.id", nullable=False)
    training: Optional[Training] = Relationship(back_populates="comments")
    author_id: int = Field(foreign_key="user.id", nullable=False)
    author: Optional[User] = Relationship(back_populates="comments")

class Event(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(nullable=False) 
    start_time: datetime = Field(nullable=False)
    end_time: datetime = Field(nullable=False)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    training_id: int = Field(foreign_key="training.id", nullable=True)
    description: str = Field(nullable=True)
    user: Optional["User"] = Relationship(back_populates="events")
    training: Optional["Training"] = Relationship()


