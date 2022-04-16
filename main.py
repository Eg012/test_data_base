import data_base
from api import add_user

if __name__ == "__main__":
    data_base.init()
    usr = add_user(user_name="Ivan",
                   pass_hash='11221',
                   first_name="Ivan")
    print(usr)
