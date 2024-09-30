from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.database import Base

class Crop(Base):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    variety = Column(String)
    planting_date = Column(String)
    expected_harvest_date = Column(String)
    field_size = Column(Float)

    yields = relationship("Yield", back_populates="crop")