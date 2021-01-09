# from sqlalchemy import Column, String, Integer, ForeignKey
# from sqlalchemy.orm import relationship
#
# from core.database import Base
#
#
# class Item(Base):
#     __tablename__ = 'items'
#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String(100))
#     category_id = Column(Integer, ForeignKey('users.id'))
#     value = Column(Integer)
#     qtd = Column(Integer)
#     category = relationship('User', back_populates='items')
#
#
# class Category(Base):
#     __tablename__ = 'categories'
#     id = Column(Integer, primary_key=True, index=True)
