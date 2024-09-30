from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class Yield(Base):
    __tablename__ = "yields"

    id = Column(Integer, primary_key=True, index=True)
    crop_id = Column(Integer, ForeignKey("crops.id"))
    harvest_date = Column(Date)
    quantity = Column(Float)
    quality = Column(Float)  # This could be a score from 0-100

    crop = relationship("Crop", back_populates="yields")