from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.statistics import get_statistics
from schema.statistics import StatisticsResponse
from service.database import get_db


router = APIRouter()

@router.get("/statistics", response_model=StatisticsResponse)
async def read_statistics(db: Session = Depends(get_db)):
    try:
        stats = get_statistics(db)
        return stats
    except Exception as e:
        return {"error": str(e)}
