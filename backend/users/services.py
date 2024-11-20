from sqlmodel import Session
from models import User
from auth.utils import get_password_hash

def create_new_user(db: Session, username: str, email: str, password: str) -> User:
    hashed_password = get_password_hash(password)
    db_user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
