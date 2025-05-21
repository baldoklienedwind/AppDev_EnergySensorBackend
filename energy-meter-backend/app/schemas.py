from pydantic import BaseModel
from datetime import datetime

class EnergyReadingBase(BaseModel):
    voltage: float
    current: float
    power: float

class EnergyReadingCreate(EnergyReadingBase):
    pass

class EnergyReading(EnergyReadingBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True