from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(name,password):
    print(name)
    user = UserModel.find_by_username(name)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    print("indide idntity")
    user_id = payload['identity']
    print(user_id)
    return UserModel.find_by_id(user_id)