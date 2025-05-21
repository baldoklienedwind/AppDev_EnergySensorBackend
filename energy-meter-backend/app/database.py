from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://energy_sensor_db_user:ju2BOAjiUkXgy0whqjyA9XHANszk1sX6@dpg-d0mq8k63jp1c738j4740-a/energy_sensor_db"
)

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

print("Loaded DATABASE_URL:", DATABASE_URL)