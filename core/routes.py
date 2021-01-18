from datetime import datetime, timedelta

import jwt

from core.db_helper import *
from core.serializers.user import User, UserCredentials
from core.tables.users import UserTable
from core.settings import *


@app.get("/")
async def root():
    return {
        "documentation": "http://localhost:8000/docs",
        "users": "http://localhost:8000/users"
    }


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


@app.post('/register')
async def register(user: AuthUser):
    if user.password != user.password2:
        return {'detail': 'As senhas não são iguais.'}
    register_authuser(db.session, user)
    return {'detail': f'Usuário {user.name} registrado.'}


@app.post('/login')
async def login(credentials: UserCredentials):
    logged = login_user(db.session, credentials)
    user = get_user_by_email(db.session, credentials.email)
    if not logged:
        return {'detail': 'Credenciais inválidas.'}
    data = {
        'user_id': user.id,
        'user_email': user.email,
        'exp': datetime.utcnow() + timedelta(days=JWT_CONFIG['exp_days'])
    }
    return {'token': jwt.encode(data, SECRET_KEY, algorithm='HS256')}
