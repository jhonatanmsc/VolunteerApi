from core.db_helper import *
from core.serializers.user import User
from core.tables.users import UserTable
from core.settings import *


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/users')
async def register_user(user: User):
    if get_user_by_email(db.session, user.email) is not None:
        return {'detail': 'already exists a user with this email'}
    instance = create_user(db.session, user)
    return {'user': instance}


@app.get('/users')
async def get_users():
    return get_objects(UserTable, db.session)


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    user_object = get_object(UserTable, db.session, user_id)
    if user_object is None:
        return {'status': 404}
    return user_object


@app.put('/users/{user_id}')
async def put_user(user_id: int, user: UpdateUser):
    instance = update_user(db.session, user_id, user)
    if instance is None:
        return {'status': 404}
    return instance


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    instance = delete_object(UserTable, db.session, user_id)
    if instance is None:
        return {'status': '404'}
    return {'status': '204'}
