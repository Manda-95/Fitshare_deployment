from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=False, nullable=False)

class Exercise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=False, nullable=False)
    id_category: int = Field(foreign_key="category.id", nullable=False)


class Training(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True, unique=False, nullable=False)
    theme: str = Field(index=True, unique=False, nullable=False)
    goal: str = Field(index=True, unique=False, nullable=False)
    difficulty: str = Field(index=True, unique=False, nullable=False)
    exercises: str = Field(index=True, unique=False, nullable=False)

class Goal(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=False, nullable=False)

