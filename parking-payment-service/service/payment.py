from sqlalchemy.orm import Session
from models.payment import Payment
from schema.payment import PaymentBase

# 새로운 결제 등록
def register(db: Session, payment: PaymentBase):
    new_payment = Payment(**payment.dict())  # dict() 메서드를 사용하여 데이터 변환
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

# 결제 목록 조회
def paymentlist(db: Session):
    return db.query(Payment).order_by(Payment.carnum.desc()).all()

# 특정 차량 번호에 따른 결제 조회
def paymentone(db: Session, carnum: str):
    return db.query(Payment).filter(Payment.carnum == carnum).all()
