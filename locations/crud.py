from sqlalchemy.orm import Session
from database.models import Location as LocationModel
from uuid import UUID


# CREATE
def create_location(db: Session, name: str):
    location = LocationModel(name=name)
    db.add(location)
    db.commit()
    db.refresh(location)
    return location


# READ
def get_location(db: Session, location_id: UUID):
    return db.query(LocationModel).filter(LocationModel.id == location_id).first()


def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(LocationModel).offset(skip).limit(limit).all()
