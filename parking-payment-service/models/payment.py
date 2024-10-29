from datetime import datetime
from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payment'

    payid = Column(VARCHAR(30), primary_key=True, index=True)
    payment = Column(VARCHAR(50), nullable=False)
    paydate = Column(VARCHAR(30), nullable=False)
    parkingtime = Column(VARCHAR(20), nullable=False)
    carnum = Column(VARCHAR(50), nullable=False) #ForeignKey=('parking.carnum'))