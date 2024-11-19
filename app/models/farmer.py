from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact = Column(String)
    farm_location = Column(String)

    # Define a relationship with the Crop model
    crops = relationship("Crop", back_populates="owner")