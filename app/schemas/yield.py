# app/schemas/yield.py

from pydantic import BaseModel
from typing import Optional

class YieldBase(BaseModel):
    quantity: float
    harvest_date: int  # Use year or a specific date format (like yyyy-mm-dd)

class YieldCreate(YieldBase):
    crop_id: int  # The crop to which this yield is related

class Yield(YieldBase):
    id: int
    crop_id: int

    class Config:
        orm_mode = True
