from sqlalchemy.sql.expression import select
from data_base import User, Session


def add_user(user_name, pass_hash, first_name):
    with Session.begin() as session:
        if session.execute(select(User).where(User.user_name == user_name)).scalar():
            raise Exception(f"User with user_name {user_name}")

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


# def get_user(user_name, , User, ):
#     with Session.begin() as session:
#         users = session.execute(select(User)).scalar().all()
#         return [
#             dict(
#                 user_name=fixed_username,
#                 pass_hash=users.pass_hash,
#                 id=users.id,
#                 first_name=users.first_name
#             )
#             for i in users
#         ]
