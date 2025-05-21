from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from .database import SessionLocal, engine, Base
from . import crud

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://appdev-energysensorwebfrontend.onrender.com",
    "exp://", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

class ReadingIn(BaseModel):
    voltage: float
    current: float
    power: float

@app.post("/api/readings")
async def post_reading(reading: ReadingIn, db: AsyncSession = Depends(get_db)):
    return await crud.create_reading(db, reading.voltage, reading.current, reading.power)

@app.get("/api/readings")
async def get_readings(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_readings(db)