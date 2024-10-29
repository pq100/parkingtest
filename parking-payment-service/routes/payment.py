
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from schema.payment import PaymentBase, Payment, PaymentList, CarNumRequest, ParkingList
from service.database import get_db
from service.payment import register, paymentlist, paymentone

router = APIRouter()

# 결제
@router.post('/payment')
async def new_payment(payment: PaymentBase, db: Session = Depends(get_db)):
    print(payment)
    return register(db, payment)

# 정산내역 (리스트 형식)
@router.get('/paycheck', response_model=list[PaymentList])
async def paycheck(db: Session = Depends(get_db)):
    paycheck = paymentlist(db)
    return [PaymentList.model_validate(p) for p in paycheck]


# 특정 정산내역
@router.get('/payment/{pno}')
async def get_paymentone(pno: int, db: Session = Depends(get_db)):
    parkings = paymentone(db, pno)
    if not parkings:
        raise HTTPException(404, '결제내역이 없습니다')
    return ParkingList.model_validate(parkings)

# @router.post('/payment')
# async def get_paymentone(request: CarNumRequest, db: Session = Depends(get_db)):
#     try:
#         payments = paymentone(db, request.carnum)
#         if not payments:
#             raise HTTPException(404, '결제내역이 없습니다')
#         return [PaymentList.model_validate(p) for p in payments]
#     except Exception as e:
#         raise HTTPException(500, f'서버 오류: {str(e)}')
