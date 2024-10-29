import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import statistics
from service.database import create_tables, get_db

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:3000",  # 허용할 프론트엔드 도메인
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(statistics.router)

# 데이터베이스 테이블 생성
create_tables()

if __name__ == '__main__':
    uvicorn.run('main:app', port=8003, reload=True)