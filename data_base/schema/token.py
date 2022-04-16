from sqlalchemy import Integer, Column, String

from .base import Base


class Token(Base):
    """Token data_base"""
    __tablename__ = "tokens"
    id = Column(String(56), primary_key=True)
