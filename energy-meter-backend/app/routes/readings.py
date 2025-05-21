from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/api", tags=["readings"])

@router.post(
    "/readings",
    response_model=schemas.EnergyReading,
    status_code=201,
)
async def create_reading(
    payload: schemas.EnergyReadingCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await crud.create_reading(
            db, payload.voltage, payload.current, payload.power
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/readings",
    response_model=list[schemas.EnergyReading],
)
async def read_readings(db: AsyncSession = Depends(get_db)):
    try:
        return await crud.get_all_readings(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))