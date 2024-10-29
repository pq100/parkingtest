from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.statistics import Statistics, PaymentList, VisitorStatsBase
from service.database import get_db
from service.statistics import register_visitor, payment_list as fetch_statistics

router = APIRouter()

@router.post('/statistics', response_model=Statistics)
async def new_statistics(visitor: VisitorStatsBase, db: Session = Depends(get_db)):
    print(visitor)
    return register_visitor(db, visitor)

@router.get('/statistics', response_model=list[PaymentList])
async def list_statistics(db: Session = Depends(get_db)):
    statistics = fetch_statistics(db)
    return [PaymentList.model_validate(u) for u in statistics]
