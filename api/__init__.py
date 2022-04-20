from sqlalchemy.sql.expression import select
from data_base import User, Session
import hashlib


def hash_password(password: str, salt=""):
    secret_bytes = password.encode()
    salt_bytes = salt.encode()
    return hashlib.pbkdf2_hmac("sha256", secret_bytes, salt_bytes, 100000).hex()


def add_user(user_name, pass_hash, first_name):
    with Session.begin() as session:
        if session.execute(select(User).where(User.user_name == user_name)).scalar():
            raise Exception('username is unique')

        new_user = User(
            user_name=user_name,
            pass_hash=pass_hash,
            firstname=first_name
        )
        session.add(new_user)
        session.flush()

        return dict(
            user_name=new_user.user_name,
            pass_hash=new_user.pass_hash,
            id=new_user.id,
            firstname=new_user.firstname
        )


def get_user(user_name):
    with Session.begin() as session:
        user = session.execute(select(User).where(User.user_name == user_name)).scalar()

        return dict(
            user_name=user.user_name,
            pass_hash=user.pass_hash,
            id=user.id,
            first_name=user.firstname
        )


def get_users():
    with Session.begin() as session:
        users = session.execute(select(User)).scalars().all()
        return [dict(user_name=u.user_name,
                     pass_hash=u.pass_hash,
                     id=u.id,
                     first_name=u.firstname
                     ) for u in users]


def register(user_name, password):
    with Session.begin() as session:
        if session.execute(select(User).where(User.user_name == user_name)).scalar():
            raise Exception('username is unique')

        new_user = User(
            user_name=user_name,
            pass_hash=hash_password(password)
        )

        session.add(new_user)
        session.flush()

        return dict(
            user_name=new_user.user_name,
            pass_hash=new_user.pass_hash,
        )


def login(user_name, password):
    with Session.begin() as session:
        user = session.execute(
            select(User).where(User.user_name == user_name).where(User.pass_hash == hash_password(password))).scalar()
        if user is None:
            raise Exception
        return dict( user_name=user.user_name,
                     pass_hash=user.pass_hash,
        )
