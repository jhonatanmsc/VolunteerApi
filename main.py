import pdb
from fastapi_sqlalchemy import db, DBSessionMiddleware

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from app.database import engine, pg
from app.models import User
from app.tables import UserTable

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=pg.postgres_db_path)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/users')
async def create_user(user: User):
    user_instance = UserTable(
        name=user.name,
        middle_name=user.middle_name,
        district=user.district,
        city=user.city
    )
    db.session.add(user_instance)
    db.session.commit()
    return user_instance
