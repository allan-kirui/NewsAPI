from pydantic import BaseModel
from typing import List
from uuid import UUID


class PersonBase(BaseModel):
    name: str
    surname: str


class PersonIDDetailsResponse(PersonBase):
    id: UUID


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: UUID

    class Config:
        orm_mode = True


class PersonListResponse(BaseModel):
    people: List[PersonIDDetailsResponse]


class PeopleID(BaseModel):
    person_id: UUID

class PersonCreateResponse(BaseModel):
    people: List[PersonCreate]

    model_config = {
        "json_schema_extra": {
            "example": {
                "people": [
                    {
                        "name": "John",
                        "surname": "Doe"
                    },
                    {
                        "name": "Jane",
                        "surname": "Doe"
                    }
                ]
            }
        }
    }
