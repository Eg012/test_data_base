from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ["Session", "engine", "init"]

DATABASE_URl = "sqlite:///database.db"

engine = create_engine(
    DATABASE_URl,
    echo=True, echo_pool=True, pool_pre_ping=True
)

Session = sessionmaker(engine, future=True)

from .schema.base import Base


def init() -> None:
    Base.metadata.create_all(engine, checkfirst=True)


def clear() -> None:
    Base.metadata.drop_all(engine, checkfirst=True)
