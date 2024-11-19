# app/api/crop_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import crop_schema
from app.crud import crop as crud
from app.db.database import get_db
from app import models

router = APIRouter()

# Create a new crop
@router.post("/", response_model=crop_schema.Crop)
def create_crop(crop: crop_schema.CropCreate, db: Session = Depends(get_db)):
    # Now `crop` will have an `owner_id` field
    owner_id = crop.owner_id
    
    # Check if the owner (farmer) exists
    owner = db.query(models.farmer.Farmer).filter(models.farmer.Farmer.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Farmer not found")

    # Create the crop
    return crud.create_crop(db=db, crop=crop, owner_id=owner_id)

# Get a specific crop by ID
@router.get("/{crop_id}", response_model=crop_schema.Crop)
def get_crop(crop_id: int, db: Session = Depends(get_db)):
    db_crop = crud.get_crop(db, crop_id=crop_id)
    if db_crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    return db_crop

# Get all crops by a specific farmer (owner)
@router.get("/farmer/{owner_id}", response_model=list[crop_schema.Crop])
def get_crops_by_farmer(owner_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    crops = crud.get_crops_by_farmer(db=db, owner_id=owner_id, skip=skip, limit=limit)
    return crops

# Base endpoint for crop operations (e.g., GET list of all crops)
@router.get("/", response_model=list[crop_schema.Crop])
def get_crops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    crops = db.query(crop_schema.Crop).offset(skip).limit(limit).all()
    return crops
