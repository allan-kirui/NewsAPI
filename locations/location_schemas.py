from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class LocationBase(BaseModel):
    name: str
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "location1"
            }
        }
    }

class LocationCreate(LocationBase):
    pass


class LocationID(BaseModel):
    location_id: UUID

    model_config = {
        "json_schema_extra": {
            "example": {
                "location_id": "550e8400-e29b-41d4-a716-446655440000"
            }
        }
    }



class LocationList(BaseModel):
    locations: List[LocationBase]

    model_config = {
        "json_schema_extra": {
            "example": {
                "locations": [
                    {
                        "name": "location1"
                    },
                    {
                        "name": "location2"
                    }
                ]
            }
        }
    }
