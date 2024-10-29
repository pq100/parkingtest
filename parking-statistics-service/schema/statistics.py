from pydantic import BaseModel
from typing import List

class VisitorStatistics(BaseModel):
    month: str
    visitor_count: int

class PaymentStatistics(BaseModel):
    month: str
    total_payment: float

class StatisticsResponse(BaseModel):
    visitordata: List[VisitorStatistics]
    paymentdata: List[PaymentStatistics]
