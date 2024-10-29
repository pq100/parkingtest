from sqlalchemy.orm import Session
from schema.statistics import VisitorStatsBase, PaymentStatsBase
from models.statistics import VisitorStats, PaymentStats
from typing import List, Optional

# 방문자 통계 등록
def register_visitor(db: Session, visitor: VisitorStatsBase) -> VisitorStats:
    try:
        visitor = VisitorStats(**visitor.model_dump())
        db.add(visitor)
        db.commit()
        db.refresh(visitor)
        return visitor
    except Exception as e:
        print(f"Error registering visitor: {e}")
        db.rollback()
        raise

# 요금 통계 등록
def register_payment(db: Session, payment: PaymentStatsBase) -> PaymentStats:
    try:
        payment = PaymentStats(**payment.model_dump())
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment
    except Exception as e:
        print(f"Error registering payment: {e}")
        db.rollback()
        raise

# 방문자 통계 목록 조회
def visitor_list(db: Session) -> List[VisitorStats]:
    return db.query(VisitorStats).all()

# 요금 통계 목록 조회
def payment_list(db: Session) -> List[PaymentStats]:
    return db.query(PaymentStats).all()

# 요금 통계 상세 조회
def payment_one(db: Session, sno: int) -> Optional[PaymentStats]:
    return db.query(PaymentStats).filter(PaymentStats.sno == sno).first()
