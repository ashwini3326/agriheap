# app/api/farmer.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import farmer_schema as farmer_schemas
from app.db import database 
from app.crud import farmer as crud


router = APIRouter()


# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a new farmer
@router.post("/", response_model=farmer_schemas.Farmer)
def create_farmer(farmer: farmer_schemas.FarmerCreate, db: Session = Depends(get_db)):
    return crud.create_farmer(db=db, farmer=farmer)


# Get a farmer by ID
@router.get("/{farmer_id}", response_model=farmer_schemas.Farmer)
def get_farmer(farmer_id: int, db: Session = Depends(get_db)):
    db_farmer = crud.get_farmer(db=db, farmer_id=farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer


# Get all farmers
@router.get("/", response_model=list[farmer_schemas.Farmer])
def get_farmers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_farmers(db=db, skip=skip, limit=limit)


# Update a farmer
@router.put("/{farmer_id}", response_model=farmer_schemas.Farmer)
def update_farmer(
    farmer_id: int, farmer: farmer_schemas.FarmerUpdate, db: Session = Depends(get_db)
):
    db_farmer = crud.update_farmer(db=db, farmer_id=farmer_id, farmer=farmer)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer


# Delete a farmer
@router.delete("/{farmer_id}", response_model=farmer_schemas.Farmer)
def delete_farmer(farmer_id: int, db: Session = Depends(get_db)):
    db_farmer = crud.delete_farmer(db=db, farmer_id=farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer
