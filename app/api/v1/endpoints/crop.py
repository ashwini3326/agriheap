from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud import crop as crop_crud
from app.schemas.crop import Crop, CropCreate
from app.db.database import get_db

router = APIRouter()

@router.post("/crops/", response_model=Crop)
def create_crop(crop: CropCreate, db: Session = Depends(get_db)):
    return crop_crud.create_crop(db=db, crop=crop)

@router.get("/crops/", response_model=List[Crop])
def read_crops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    crops = crop_crud.get_crops(db, skip=skip, limit=limit)
    return crops

@router.get("/crops/{crop_id}", response_model=Crop)
def read_crop(crop_id: int, db: Session = Depends(get_db)):
    db_crop = crop_crud.get_crop(db, crop_id=crop_id)
    if db_crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    return db_crop

@router.put("/crops/{crop_id}", response_model=Crop)
def update_crop(crop_id: int, crop: CropCreate, db: Session = Depends(get_db)):
    db_crop = crop_crud.update_crop(db, crop_id=crop_id, crop=crop)
    if db_crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    return db_crop

@router.delete("/crops/{crop_id}", response_model=Crop)
def delete_crop(crop_id: int, db: Session = Depends(get_db)):
    db_crop = crop_crud.delete_crop(db, crop_id=crop_id)
    if db_crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    return db_crop