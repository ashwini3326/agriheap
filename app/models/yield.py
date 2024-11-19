from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Yield(Base):
    __tablename__ = 'yields'

    id = Column(Integer, primary_key=True, index=True)
    crop_id = Column(Integer, ForeignKey("crops.id"), nullable=False)
    quantity = Column(Float, nullable=False)  # The amount of crop harvested
    harvest_date = Column(Integer, nullable=False)  # Year/Date of harvest

    crop = relationship("Crop", back_populates="yields")
