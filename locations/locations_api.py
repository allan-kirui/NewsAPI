from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import Database
from locations import locations_crud, location_schemas

router = APIRouter()


# GETS
# @router.get("/{location_id}")
# async def read_location(location_id: UUID, db: Session = Depends(Database().get_db)):
#     location = locations_crud.get_location(db, location_id)
#     if location is None:
#         raise HTTPException(status_code=404, detail="Location does not exist")
#     return location

# lists a location based on provided location_id
@router.get("/", response_model=location_schemas.LocationIDDetailsResponse)
async def read_location(location_id: location_schemas.LocationID = Depends(), db: Session = Depends(Database().get_db)):
    location = locations_crud.get_location(db, location_id.location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location does not exist")
    return location


@router.get("/list/")
async def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(Database().get_db)):
    locations = locations_crud.get_locations(db, skip=skip, limit=limit)
    return locations


# POST
@router.post("/", response_model=location_schemas.LocationBase)
async def create_location(location: location_schemas.LocationBase, db: Session = Depends(Database().get_db)):
    try:
        return locations_crud.create_location(db=db, name=location.name)
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/multiple/")
async def create_locations(locations: location_schemas.LocationCreateResponse, db: Session = Depends(Database().get_db)):
    list_locations = []
    for location in locations.locations:
        list_locations.append(location.name)
    return locations_crud.create_locations_bulk(db=db, names=list_locations)


# DELETE
@router.delete("/{location_id}")
async def delete_location(location_id: UUID, db: Session = Depends(Database().get_db)):
    location = locations_crud.get_location(db, location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location does not exist")
    db.delete(location)
    db.commit()
    return location
