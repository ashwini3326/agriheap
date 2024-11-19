from sqlalchemy.orm import Session
from app.models import farmer as models
from app.models import crop
from app.schemas import farmer_schema as farmer_schemas


# Create a new farmer
def create_farmer(db: Session, farmer: farmer_schemas.FarmerCreate):
    db_farmer = models.Farmer(
        name=farmer.name,
        contact=farmer.contact,
        farm_location=farmer.farm_location,
    )
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer


# Get a farmer by ID
def get_farmer(db: Session, farmer_id: int):
    return db.query(models.Farmer).filter(models.Farmer.id == farmer_id).first()


# Get all farmers
def get_farmers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Farmer).offset(skip).limit(limit).all()


# Update a farmer
def update_farmer(db: Session, farmer_id: int, farmer: farmer_schemas.FarmerUpdate):
    db_farmer = db.query(models.Farmer).filter(models.Farmer.id == farmer_id).first()
    if db_farmer:
        db_farmer.name = farmer.name if farmer.name else db_farmer.name
        db_farmer.contact = farmer.contact if farmer.contact else db_farmer.contact
        db_farmer.farm_location = farmer.farm_location if farmer.farm_location else db_farmer.farm_location
        db.commit()
        db.refresh(db_farmer)
    return db_farmer


# Delete a farmer
def delete_farmer(db: Session, farmer_id: int):
    db_farmer = db.query(models.Farmer).filter(models.Farmer.id == farmer_id).first()
    if db_farmer:
        db.delete(db_farmer)
        db.commit()
    return db_farmer
