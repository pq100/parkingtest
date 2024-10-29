# from datetime import datetime
# from sqlalchemy import Column, VARCHAR, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
# #
# # class Payment(Base):
# #     __tablename__ = 'payment'
# #
# #     payid = Column(VARCHAR(30), primary_key=True, index=True)
# #     payment = Column(VARCHAR(50), nullable=False)
# #     paydate = Column(VARCHAR(30), nullable=False)
# #     parkingtime = Column(VARCHAR(20), nullable=False)
# #     carnum = Column(VARCHAR(50), nullable=False) #ForeignKey=('parking.carnum'))


from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Parking(Base):
    __tablename__ = 'parking'

    pno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    carnum = Column(String(10), nullable=False)
    barrier = Column(String(5), nullable=False, default='0')
    intime = Column(DateTime, default=datetime.now)
    outtime = Column(DateTime, nullable=True)


class Parkseat(Base):
    __tablename__ = 'parkseat'

    carnum = Column(String(10), primary_key=True, nullable=False)
    barrier = Column(String(5), nullable=False, default='0')

# 수정 필요
class Payment(Base):
    __tablename__ = 'payment'

    payid = Column(String(30), primary_key=True, index=True)
    payment = Column(String(50))
    paydate = Column(DateTime, nullable=True)
    parkingtime = Column(String(20), nullable=True)
    carnum = Column(String(10), ForeignKey('parking.carnum'))

class VisitorStats(Base):
    __tablename__ = 'visitor_stats'

    sno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    carnum = Column(String(10), nullable=False)
    month = Column(String(10), nullable=False)
    visitor_count = Column(Integer, nullable=False)


class PaymentStats(Base):
    __tablename__ = 'payment_stats'

    sno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    month = Column(String(10), nullable=False)
    total_fee = Column(Float, nullable=False)