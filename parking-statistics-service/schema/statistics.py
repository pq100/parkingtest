from pydantic import BaseModel
from typing import List

class VisitorStatsBase(BaseModel):
    month: str
    visitor_count: int

class VisitorStats(VisitorStatsBase):
    sno: int

    class Config:
        from_attributes = True

class PaymentStatsBase(BaseModel):
    month: str
    total_fee: float  # 요금을 만원 단위로 저장

class PaymentStats(PaymentStatsBase):
    sno: int

    class Config:
        from_attributes = True

class PaymentList(BaseModel):
    sno: int
    carnum: str
    payid: str
    parkingtime: str

    class Config:
        from_attributes = True

class Statistics(BaseModel):
    visitors: List[VisitorStats]
    payments: List[PaymentStats]

    class Config:
        from_attributes = True
