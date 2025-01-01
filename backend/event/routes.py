from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database import get_db
from models import Event, User
from schemas import EventCreate, EventResponse
from auth.utils import get_current_user

router = APIRouter()

@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérification du chevauchement d'événements
    overlapping_event = db.query(Event).filter(
        Event.user_id == current_user.id,
        Event.start_time < event.end_time,
        Event.end_time > event.start_time,
    ).first()

    if overlapping_event:
        raise HTTPException(
            status_code=400,
            detail="Chevauchement avec un autre événement existant.",
        )

    # Création de l'événement
    new_event = Event(
        title=event.title,
        start_time=event.start_time,
        end_time=event.end_time,
        user_id=current_user.id,
        training_id=event.training_id,
        description=event.description,
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.get("/", response_model=list[EventResponse], status_code=status.HTTP_200_OK)
def get_user_events(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    events = db.query(Event).filter(Event.user_id == current_user.id).all()
    return events
