from sqlalchemy.orm import Session
from sqlalchemy import extract, func
from models.statistics import Payment  # 경로 조정 필요
from schema.statistics import StatisticsResponse

def get_monthly_payments(db: Session):
    monthly_payments = [0] * 12
    results = db.query(
        extract('month', Payment.paydate).label('month'),
        func.sum(Payment.payment).label('total_payment')
    ).group_by('month').all()

    for month, total_payment in results:
        monthly_payments[int(month) - 1] = total_payment

    return monthly_payments

def get_monthly_visitors(db: Session):
    monthly_visitors = [0] * 12
    # 방문자 수를 가져오는 로직을 여기에 추가하세요.
    return monthly_visitors

def get_statistics(db: Session) -> StatisticsResponse:
    monthly_payments = get_monthly_payments(db)
    monthly_visitors = get_monthly_visitors(db)

    visitordata = [{"month": str(i + 1), "visitor_count": count} for i, count in enumerate(monthly_visitors)]
    paymentdata = [{"month": str(i + 1), "total_payment": total} for i, total in enumerate(monthly_payments)]

    return StatisticsResponse(visitordata=visitordata, paymentdata=paymentdata)
