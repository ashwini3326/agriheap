from sqlalchemy.orm import Session
from app.models.yield import Yield
from app.schemas.yield import YieldCreate

def get_yield(db: Session, yield_id: int):
    return db.query(Yield).filter(Yield.id == yield_id).first()

def get_yields(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Yield).offset(skip).limit(limit).all()

def create_yield(db: Session, yield_data: YieldCreate):
    db_yield = Yield(**yield_data.dict())
    db.add(db_yield)
    db.commit()
    db.refresh(db_yield)
    return db_yield

def update_yield(db: Session, yield_id: int, yield_data: YieldCreate):
    db_yield = get_yield(db, yield_id)
    if db_yield:
        for key, value in yield_data.dict().items():
            setattr(db_yield, key, value)
        db.commit()
        db.refresh(db_yield)
    return db_yield

def delete_yield(db: Session, yield_id: int):
    db_yield = get_yield(db, yield_id)
    if db_yield:
        db.delete(db_yield)
        db.commit()
    return db_yield

def get_yields_by_crop(db: Session, crop_id: int):
    return db.query(Yield).filter(Yield.crop_id == crop_id).all()