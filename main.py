import data_base
from api import add_user
from api import get_user
from api import get_users, hash_password, register, login
if __name__ == "__main__":
    data_base.init()
    # usr = add_user(user_name="Ivan10",
    #                pass_hash='11221',
    #                first_name="Ivan")
    # print(usr)
    #
    # data_base.init()
    # user = get_user(user_name="Ivan")
    #
    #
    # print(user)

    # users = get_users()

    # print(users)



    # print(hash_password("Hello"), hash_password("Hello", "1234"))

    # reg = register(user_name="Ivan11",
    #                password="11221",
    #                )
    # print(reg)
    log = login(user_name="Ivan11",
                password="1121")
    print(log)