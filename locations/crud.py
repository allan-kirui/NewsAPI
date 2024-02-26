from sqlalchemy.orm import Session
from database import models
from uuid import UUID


def get_location(db: Session, location_id: UUID):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Location).offset(skip).limit(limit).all()
