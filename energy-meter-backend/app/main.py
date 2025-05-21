from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime
import random

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://appdev-energysensorwebfrontend.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EnergyReading(BaseModel):
    voltage: float
    current: float
    power: float
    timestamp: datetime

readings: List[EnergyReading] = []

@app.get("/api/readings", response_model=List[EnergyReading])
async def get_readings():
    voltage = round(random.uniform(110.0, 130.0), 2)
    current = round(random.uniform(5.0, 15.0), 2)
    power = round(voltage * current, 2)
    timestamp = datetime.utcnow()

    reading = EnergyReading(
        voltage=voltage,
        current=current,
        power=power,
        timestamp=timestamp
    )
    readings.append(reading)
    return readings