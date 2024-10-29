from models.statistics import Payment
from sqlalchemy.orm import Session
from datetime import datetime
from collections import defaultdict

def get_statistics(db: Session):
    # 현재 연도 가져오기
    current_year = datetime.now().year

    # 데이터 초기화
    visitor_data = defaultdict(int)
    payment_data = defaultdict(float)

    # 모든 결제 기록 조회
    payments = db.query(Payment).all()

    for payment in payments:
        if payment.paydate:
            pay_date = payment.paydate  # 이미 DateTime 형식이라 변환할 필요 없음
            month = pay_date.strftime("%m")  # 문자열로 월 추출

            # 방문자 수 카운트
            visitor_data[month] += 1  # 해당 월의 방문자 수 증가
            # 결제 합산
            payment_data[month] += payment.payment  # 결제가 Float으로 저장됨

    # 응답을 위한 결과 포맷팅
    visitordata = [{"month": month, "visitor_count": count} for month, count in sorted(visitor_data.items())]
    paymentdata = [{"month": month, "total_payment": total} for month, total in sorted(payment_data.items())]

    return {
        "visitordata": visitordata,
        "paymentdata": paymentdata,
    }
