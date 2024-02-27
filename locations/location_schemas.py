from typing import List
from uuid import UUID

from pydantic import BaseModel


class LocationBase(BaseModel):
    name: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: UUID

    class Config:
        orm_mode = True


class LocationList(BaseModel):
    locations: List[LocationBase]
