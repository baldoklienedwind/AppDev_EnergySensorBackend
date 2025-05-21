from pydantic import BaseModel
from datetime import datetime

class EnergyReadingCreate(BaseModel):
    voltage: float
    current: float
    power: float