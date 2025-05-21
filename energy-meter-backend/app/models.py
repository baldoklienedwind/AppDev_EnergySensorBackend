from sqlalchemy import Column, Float, Integer, DateTime, func
from .database import Base

class EnergyReading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    voltage = Column(Float, nullable=False)
    current = Column(Float, nullable=False)
    power = Column(Float, nullable=False)
    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )