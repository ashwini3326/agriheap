from pydantic import BaseModel

class CropBase(BaseModel):
    name: str
    variety: str
    planting_date: str
    expected_harvest_date: str
    field_size: float

class CropCreate(CropBase):
    pass

class Crop(CropBase):
    id: int

    class Config:
        orm_mode = True