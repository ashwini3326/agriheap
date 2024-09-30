from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud import yield as yield_crud
from app.schemas.yield import Yield, YieldCreate
from app.db.database import get_db

router = APIRouter()

@router.post("/yields/", response_model=Yield)
def create_yield(yield_data: YieldCreate, db: Session = Depends(get_db)):
    return yield_crud.create_yield(db=db, yield_data=yield_data)

@router.get("/yields/", response_model=List[Yield])
def read_yields(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    yields = yield_crud.get_yields(db, skip=skip, limit=limit)
    return yields

@router.get("/yields/{yield_id}", response_model=Yield)
def read_yield(yield_id: int, db: Session = Depends(get_db)):
    db_yield = yield_crud.get_yield(db, yield_id=yield_id)
    if db_yield is None:
        raise HTTPException(status_code=404, detail="Yield not found")
    return db_yield

@router.put("/yields/{yield_id}", response_model=Yield)
def update_yield(yield_id: int, yield_data: YieldCreate, db: Session = Depends(get_db)):
    db_yield = yield_crud.update_yield(db, yield_id=yield_id, yield_data=yield_data)
    if db_yield is None:
        raise HTTPException(status_code=404, detail="Yield not found")
    return db_yield

@router.delete("/yields/{yield_id}", response_model=Yield)
def delete_yield(yield_id: int, db: Session = Depends(get_db)):
    db_yield = yield_crud.delete_yield(db, yield_id=yield_id)
    if db_yield is None:
        raise HTTPException(status_code=404, detail="Yield not found")
    return db_yield

@router.get("/crops/{crop_id}/yields", response_model=List[Yield])
def read_yields_by_crop(crop_id: int, db: Session = Depends(get_db)):
    yields = yield_crud.get_yields_by_crop(db, crop_id=crop_id)
    return yields