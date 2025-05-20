from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import EnergyReading

async def create_reading(db: AsyncSession, voltage: float, current: float, power: float, energy: float):
    reading = EnergyReading(voltage=voltage, current=current, power=power, energy=energy)
    db.add(reading)
    await db.commit()
    await db.refresh(reading)
    return reading

async def get_all_readings(db: AsyncSession):
    result = await db.execute(select(EnergyReading))
    return result.scalars().all()