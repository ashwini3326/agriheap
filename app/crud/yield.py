# app/crud/yield.py

from sqlalchemy.orm import Session
from app import models, schemas

def create_yield(db: Session, yield_: schemas.YieldCreate):
    db_yield = models.Yield(
        crop_id=yield_.crop_id,
        quantity=yield_.quantity,
        harvest_date=yield_.harvest_date
    )
    db.add(db_yield)
    db.commit()
    db.refresh(db_yield)
    return db_yield

def get_yield(db: Session, yield_id: int):
    return db.query(models.Yield).filter(models.Yield.id == yield_id).first()

def get_yields_by_crop(db: Session, crop_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Yield).filter(models.Yield.crop_id == crop_id).offset(skip).limit(limit).all()

def get_all_yields(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Yield).offset(skip).limit(limit).all()

def delete_yield(db: Session, yield_id: int):
    db_yield = db.query(models.Yield).filter(models.Yield.id == yield_id).first()
    if db_yield:
        db.delete(db_yield)
        db.commit()
        return db_yield
    return None
