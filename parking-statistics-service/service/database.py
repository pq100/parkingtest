import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.statistics import Base

# 현재 파일 위치에 따라 parking.db 위치 설정
db_path = os.path.join(os.path.dirname(__file__), '..', 'parking.db')
db_url = 'sqlite:///../parking.db'

engine = create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def get_db():
    with SessionLocal() as db:
        yield db
