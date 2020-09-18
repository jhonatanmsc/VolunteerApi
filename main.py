import pdb
from fastapi_sqlalchemy import db, DBSessionMiddleware

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from app.database import engine, pg
from app.models import User, Action
from app.tables import UserTable, ActionsTable

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
    return {'status': '201'}


@app.get('/users')
async def get_users():
    return db.session.query(UserTable).offset(0).all()


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    return db.session.query(UserTable).filter(UserTable.id == user_id).first()


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    user_instance = db.session.query(UserTable).filter(UserTable.id == user_id).first()
    db.session.delete(user_instance)
    db.session.commit()
    return {'status': '200'}


@app.post('/actions')
async def create_action(action: Action):
    action_instance = ActionsTable(
        name=action.name,
        company=action.company,
        street=action.street,
        number=action.number,
        district=action.district,
        city=action.city,
        description=action.description
    )
    db.session.add(action_instance)
    db.session.commit()
    return {'status': '201'}


@app.get('/actions')
async def get_actions():
    return db.session.query(ActionsTable).offset(0).all()


@app.get('/actions/{action_id}')
async def get_action(action_id: int):
    return db.session.query(ActionsTable).filter(ActionsTable.id == action_id).first()


@app.delete('/actions/{action_id}')
async def delete_action(action_id: int):
    action_instance = db.session.query(ActionsTable).filter(ActionsTable.id == action_id).first()
    db.session.delete(action_instance)
    db.session.commit()
    return {'status': '200'}
