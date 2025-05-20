from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://energy_meter_db_ag2t_user:FTPqi2yChZrdvcaxsXqOy9siodJg0I0Z@dpg-d0m3lip5pdvs738si0sg-a/energy_meter_db_ag2t"
)

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

print("Loaded DATABASE_URL:", DATABASE_URL)