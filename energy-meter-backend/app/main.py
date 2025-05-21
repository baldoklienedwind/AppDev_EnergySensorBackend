from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
import logging

from .database import SessionLocal, engine, Base
from . import crud

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

@app.on_event("startup")
async def startup():
    logger.info("Starting up, creating database tables if not exist...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Startup complete.")

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

class ReadingIn(BaseModel):
    voltage: float
    current: float
    power: float

@app.post("/api/readings")
async def post_reading(reading: ReadingIn, db: AsyncSession = Depends(get_db)):
    try:
        created = await crud.create_reading(db, reading.voltage, reading.current, reading.power)
        return created
    except Exception as e:
        logger.error(f"Error creating reading: {e}")
        raise HTTPException(status_code=500, detail="Failed to create reading")

@app.get("/api/readings")
async def get_readings(db: AsyncSession = Depends(get_db)):
    try:
        readings = await crud.get_all_readings(db)
        return readings
    except Exception as e:
        logger.error(f"Error fetching readings: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch readings")