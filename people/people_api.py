from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import Database
from people import people_crud, people_schemas

router = APIRouter()


@router.get("/", response_model=people_schemas.PersonIDDetailsResponse)
async def read_person(person_id: people_schemas.PeopleID = Depends(), db: Session = Depends(Database().get_db)):
    person = people_crud.get_person(db, person_id.person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Location does not exist")
    return person


@router.get("/list/")
async def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(Database().get_db)):
    people = people_crud.get_people(db, skip=skip, limit=limit)
    return people


# POST
@router.post("/", response_model=people_schemas.PersonBase)
async def create_person(person: people_schemas.PersonCreate, db: Session = Depends(Database().get_db)):
    try:
        return people_crud.create_person(db=db, person=person)
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/multiple/")
async def create_people(people: people_schemas.PersonCreateResponse, db: Session = Depends(Database().get_db)):
    list_people = []
    for person in people.people:
        list_people.append(person)
    return people_crud.create_people_bulk(db=db, people=list_people)
