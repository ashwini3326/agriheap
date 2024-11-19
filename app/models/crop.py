from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Crop(Base):
    __tablename__ = 'crops'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    variety = Column(String, nullable=True)
    planting_date = Column(Date, nullable=True)
    expected_harvest_date = Column(Date, nullable=True)
    field_size = Column(Float, nullable=True)
    
    # Foreign key to the Farmer model
    owner_id = Column(Integer, ForeignKey('farmers.id'))

    # Define the relationship to the Farmer model
    owner = relationship("Farmer", back_populates="crops")