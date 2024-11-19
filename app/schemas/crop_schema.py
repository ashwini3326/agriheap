from pydantic import BaseModel

class CropBase(BaseModel):
    name: str

class CropCreate(BaseModel):
    name: str
    owner_id: int  # Ensure owner_id is included here

    class Config:
        orm_mode = True  # This ensures it works well with SQLAlchemy models


class Crop(CropBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy models as dictionaries
