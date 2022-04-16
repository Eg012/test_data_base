import string
from sqlalchemy import Integer, Column, String

from .base import Base


class User(Base):
    """Users data_base"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(78), index=True, unique=True)
    pass_hash = Column(String(100), nullable=True, default=True)
    firstname = Column(String(52), nullable=True)
