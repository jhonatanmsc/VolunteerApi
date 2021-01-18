import pdb

from cryptography.fernet import Fernet
from sqlalchemy.orm import Session

from core.serializers.user import User, UpdateUser, AuthUser, UserCredentials
from core.settings import SECRET_KEY
from core.tables import UserTable


def get_object(model: any, session: Session, id: int):
    return session.query(model).filter(model.id == id).first()


def get_objects(model: any, session: Session, skip: int = 0, limit: int = 100):
    return session.query(model).offset(skip).limit(limit).all()


def delete_object(model: any, session: Session, id: int):
    user_instance = get_object(model, session, id)
    if user_instance is None:
        return None
    session.delete(user_instance)
    session.commit()
    return user_instance


def create_user(session: Session, user: User):
    instance = UserTable(
        name=user.name,
        email=user.email,
        district=user.district,
        city=user.city
    )
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def register_authuser(session: Session, user: User):
    password = Fernet(SECRET_KEY).encrypt(user.password.encode())
    instance = UserTable(
        name=user.name,
        password=password.decode(),
        email=user.email,
        district=user.district,
        city=user.city
    )
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def login_user(session: Session, credentials: UserCredentials):
    user = get_user_by_email(session, credentials.email)
    decrypted_password = Fernet(SECRET_KEY).decrypt(user.password.encode())
    return decrypted_password.decode() == credentials.password


def set_password(session: Session, id: int, password: str):
    user = get_object(UserTable, session, id)
    user.password = password
    session.add(user)
    session.commit()
    session.refresh(user)


def update_user(session: Session, user_id: int, user: UpdateUser):
    instance = get_object(UserTable, session, user_id)
    if instance is None:
        return None
    instance.district = user.district
    instance.city = user.city
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def get_user_by_email(session: Session, email: str):
    return session.query(UserTable).filter(UserTable.email == email).first()