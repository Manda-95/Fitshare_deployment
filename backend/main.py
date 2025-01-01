from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from database import create_db_and_tables
from auth.routes import router as auth_router
from users.routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from category.routes import router as category_router
from exercises.routes import router as exercises_router
from goal.routes import router as goal_router
from training.routes import router as training_router
from comment.routes import router as comment_router
from event.routes import router as event_router

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(category_router, prefix="/category", tags=["Category"])
app.include_router(exercises_router, prefix="/exercises", tags=["Exercise"])
app.include_router(goal_router, prefix="/goal", tags=["Goal"])
app.include_router(training_router, prefix="/trainings", tags=["Training"])
app.include_router(comment_router, prefix="/comments", tags=["Comments"])
app.include_router(event_router, prefix="/events", tags=["Events"])

