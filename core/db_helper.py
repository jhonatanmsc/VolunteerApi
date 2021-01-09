from sqlalchemy.orm import Session

from core.serializers.user import User, UpdateUser
from core.tables import UserTable


def get_object(model: any, session: Session, id: int):
    return session.query(model).filter(model.id == id).first()


def get_objects(model: any, session: Session, skip: int = 0, limit: int = 100):
    return session.query(model).offset(skip).limit(limit).all()


def delete_object(model: any, session: Session, id: int):
    user_instance = get_object(model, session, id)
    if user_instance is None:
        return None
    session.session.delete(user_instance)
    session.session.commit()
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