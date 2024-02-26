from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import Database
from . import crud
from database import database

router = APIRouter()


@router.get("/locations/{location_id}")
def read_location(location_id, db: Session = Depends(db_instance.get_session)):
    location = crud.get_location(db, location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location does not exist")
    return location
