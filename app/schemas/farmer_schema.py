# app/schemas/farmer.py

from pydantic import BaseModel
from typing import Optional


# Schema for creating a new farmer
class FarmerCreate(BaseModel):
    name: str
    contact: str
    farm_location: str

    class Config:
        orm_mode = True


# Schema for updating a farmer
class FarmerUpdate(BaseModel):
    name: Optional[str] = None
    contact: Optional[str] = None
    farm_location: Optional[str] = None

    class Config:
        orm_mode = True


# Schema for displaying a farmer
class Farmer(BaseModel):
    id: int
    name: str
    contact: str
    farm_location: str

    class Config:
        orm_mode = True
