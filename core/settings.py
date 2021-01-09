import logging

from fastapi import FastAPI
from fastapi_sqlalchemy import db, DBSessionMiddleware
from sqlalchemy.orm import sessionmaker

from core.database import engine, DATABASES

log = logging.getLogger()
log.setLevel(logging.DEBUG)

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DATABASES['default'])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
