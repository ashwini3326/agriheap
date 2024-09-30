from pydantic import BaseModel
from datetime import date

class YieldBase(BaseModel):
    crop_id: int
    harvest_date: date
    quantity: float
    quality: float

class YieldCreate(YieldBase):
    pass

class Yield(YieldBase):
    id: int

    class Config:
        orm_mode = True