from typing import List

from sqlalchemy.orm import Session
from uuid import UUID
from .people_schemas import PersonCreate
from database.models import Person as PersonModel


# CREATE
def create_person(db: Session, person: PersonCreate):
    db_person = PersonModel(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def create_people_bulk(db: Session, people: List[PersonCreate]):
    created_people = []
    for person in people:
        db_person = create_person(db, person)
        created_people.append(db_person)
    return created_people

def get_person(db: Session, person_id: UUID):
    return db.query(PersonModel).filter(PersonModel.id == person_id).first()


def get_people(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PersonModel).offset(skip).limit(limit).all()

def delete_person(db: Session, person_id: UUID):
    person = get_person(db, person_id)
    if person:
        db.delete(person)
        db.commit()
        return person
    return None
