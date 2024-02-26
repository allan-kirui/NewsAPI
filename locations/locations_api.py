from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import Database
from locations import locations_crud, location_schemas

router = APIRouter()


# GETS
@router.get("/{location_id}")
def read_location(location_id: UUID, db: Session = Depends(Database().get_db)):
    location = locations_crud.get_location(db, location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location does not exist")
    return location


@router.get("/")
def read_locations(skip: int = 0, limit: int = 10, db: Session = Depends(Database().get_db)):
    locations = locations_crud.get_locations(db, skip=skip, limit=limit)
    return locations


# POST
@router.post("/")
def create_location(location: location_schemas.LocationBase, db: Session = Depends(Database().get_db)):
    try:
        return locations_crud.create_location(db=db, name=location.name)
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
