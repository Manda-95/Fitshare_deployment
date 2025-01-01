from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from database import get_db
from schemas import TrainingResponse, TrainingCreate,CreatorResponse, ExerciseResponse, CommentResponse, UserResponse
from models import Training, User, Goal, Exercise, Comment
from typing import List
import json
from sqlalchemy.orm import joinedload
from auth.utils import get_current_user

router = APIRouter()

@router.post("/", response_model=TrainingResponse, status_code=status.HTTP_201_CREATED)
def create_training(
    training: TrainingCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)  # Obtenir l'utilisateur connecté
):
    # Vérifier si le Goal existe
    goal = db.get(Goal, training.goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")

    # Créer l'entraînement
    db_training = Training(
        title=training.title,
        description=training.description,
        category_id=training.category_id,
        goal_id=training.goal_id,
        difficulty=training.difficulty,
        creator_id=current_user.id  # Utiliser l'utilisateur connecté comme créateur
    )
    db.add(db_training)
    db.commit()

    # Associer les exercices
    try:
        for exercise_id in training.exercises:
            exercise = db.get(Exercise, exercise_id)
            if not exercise:
                raise HTTPException(status_code=404, detail=f"Exercise with ID {exercise_id} not found")
            db_training.exercises.append(exercise)  # Ajouter chaque exercice
    except TypeError as e:
        raise HTTPException(status_code=400, detail="Exercises must be provided as a list of IDs") from e

    db.commit()
    db.refresh(db_training)

    # Charger les relations avant de renvoyer
    db_training = db.query(Training).options(
        joinedload(Training.creator),
        joinedload(Training.category),
        joinedload(Training.goal),
        joinedload(Training.exercises),
        joinedload(Training.comments)  # Charger les commentaires, initialement vide
    ).filter_by(id=db_training.id).first()

    return TrainingResponse(
        id=db_training.id,
        title=db_training.title,
        description=db_training.description,
        category=db_training.category.name,
        goal=db_training.goal.name,
        difficulty=db_training.difficulty,
        exercises=[
            {"id": exercise.id, "name": exercise.name, "id_category": exercise.id_category}
            for exercise in db_training.exercises
        ],
        comments=[],  # Initialiser les commentaires à une liste vide
        creator=CreatorResponse(
            id=db_training.creator.id,
            username=db_training.creator.username,
            email=db_training.creator.email
        )
    )



@router.get("/", response_model=List[TrainingResponse], status_code=status.HTTP_200_OK)
def get_trainings(db: Session = Depends(get_db)):
    trainings = db.query(Training).options(
        joinedload(Training.creator),
        joinedload(Training.goal),
        joinedload(Training.exercises),
        joinedload(Training.comments).joinedload(Comment.author)  # Charger les commentaires et leurs auteurs
    ).all()

    if not trainings:
        raise HTTPException(status_code=404, detail="No trainings found")

    return [
        TrainingResponse(
            id=training.id,
            title=training.title,
            description=training.description,
            category=training.category.name,
            goal=training.goal.name,
            difficulty=training.difficulty,
            exercises=[
                ExerciseResponse(
                    id=exercise.id,
                    name=exercise.name,
                    id_category=exercise.id_category
                )
                for exercise in training.exercises
            ],
            comments=[
                CommentResponse(
                    id=comment.id,
                    content=comment.content,
                    created_at=comment.created_at,
                    training_id=training.id,  # Ajouter correctement `training_id`
                    author=UserResponse(  # Convertir en `UserResponse` attendu
                        id=comment.author.id,
                        username=comment.author.username,
                        email=comment.author.email
                    ) if comment.author else None
                )
                for comment in training.comments
            ],
            creator=CreatorResponse(
                id=training.creator.id,
                username=training.creator.username,
                email=training.creator.email
            )
        )
        for training in trainings
    ]


@router.get("/{training_id}/comments", response_model=List[CommentResponse])
def get_comments_for_training(training_id: int, db: Session = Depends(get_db)):
    training = db.get(Training, training_id)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")

    comments = db.query(Comment).options(
        joinedload(Comment.author)
    ).filter(Comment.training_id == training_id).all()

    return [
        CommentResponse(
            id=comment.id,
            content=comment.content,
            created_at=comment.created_at,
            training_id=comment.training_id,
            author={
                "id": comment.author.id,
                "username": comment.author.username,
                "email": comment.author.email,
            }
        )
        for comment in comments
    ]


@router.get("/{training_id}", response_model=TrainingResponse)
def get_training(training_id: int, db: Session = Depends(get_db)):
    training = db.query(Training).filter_by(id=training_id).first()
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")

    return TrainingResponse(
        id=training.id,
        title=training.title,
        description=training.description,
        difficulty=training.difficulty,
        category=training.category.name,
        goal=training.goal.name,
        exercises=[
            {"id": exercise.id, "name": exercise.name, "id_category": exercise.id_category}
            for exercise in training.exercises
        ],
        creator={
            "id": training.creator.id,
            "username": training.creator.username,
            "email": training.creator.email,
        },
        comments=[
            {
                "id": comment.id,
                "content": comment.content,
                "created_at": comment.created_at,
                "training_id": comment.training_id or training.id,  # Ajout d'une valeur par défaut
                "author": {
                    "id": comment.author.id,
                    "username": comment.author.username,
                    "email": comment.author.email,
                },
            }
            for comment in training.comments
        ],
    )
