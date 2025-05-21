from sqlalchemy import Column, Float, Integer, DateTime, func
from .database import Base

class EnergyReading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    voltage = Column(Float)     
    current = Column(Float)
    power = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())