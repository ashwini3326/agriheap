from sqlalchemy.orm import Session
from app.models.crop import Crop
from app.schemas.crop import CropCreate

def get_crop(db: Session, crop_id: int):
    return db.query(Crop).filter(Crop.id == crop_id).first()

def get_crops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Crop).offset(skip).limit(limit).all()

def create_crop(db: Session, crop: CropCreate):
    db_crop = Crop(**crop.dict())
    db.add(db_crop)
    db.commit()
    db.refresh(db_crop)
    return db_crop

def update_crop(db: Session, crop_id: int, crop: CropCreate):
    db_crop = get_crop(db, crop_id)
    if db_crop:
        for key, value in crop.dict().items():
            setattr(db_crop, key, value)
        db.commit()
        db.refresh(db_crop)
    return db_crop

def delete_crop(db: Session, crop_id: int):
    db_crop = get_crop(db, crop_id)
    if db_crop:
        db.delete(db_crop)
        db.commit()
    return db_crop