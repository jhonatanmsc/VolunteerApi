from sqlalchemy import Column, Integer, MetaData, String, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    middle_name = Column(String)
    district = Column(String)
    city = Column(String)


class ActionsTable(Base):
    __tablename__ = 'user_actions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company = Column(String)
    street = Column(String)
    number = Column(String)
    district = Column(String)
    city = Column(String)
    description = Column(String)


metadata = Base.metadata
