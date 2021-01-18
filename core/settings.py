import logging

from decouple import config as env
from fastapi import FastAPI
from fastapi_sqlalchemy import db, DBSessionMiddleware
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

from core.database import engine, DATABASES

log = logging.getLogger()
log.setLevel(logging.DEBUG)

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DATABASES['default'])

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

JWT_CONFIG = {
    'exp_days': 2,
}

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SECRET_KEY = env('SECRET_KEY')


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
