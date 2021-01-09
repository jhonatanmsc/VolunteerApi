from sqlalchemy import Column, String, Integer

from core.database import Base


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    district = Column(String)
    city = Column(String)

    def __str__(self):
        return f'<User: id={self.id}, name={self.name}>'
