from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database import get_db
from models import Comment, Training, User
from schemas import CommentCreate, CommentResponse
from auth.utils import get_current_user

router = APIRouter()

@router.post("/", response_model=CommentResponse, status_code=201)
def create_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifier si le training existe
    training = db.get(Training, comment.training_id)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")

    # Créer le commentaire avec l'utilisateur actuel
    new_comment = Comment(
        content=comment.content,
        training_id=comment.training_id,
        author_id=current_user.id,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return CommentResponse(
        id=new_comment.id,
        content=new_comment.content,
        created_at=new_comment.created_at,
        training_id=new_comment.training_id,
        author={
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
        }
    )
