from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

USERS = [
    {
        "id": 1,
        "name": "admin",
        "password": generate_password_hash('123')
    },
    {
        "id": 2,
        "name": "李四",
        "password": generate_password_hash('123')
    },
]


class User(UserMixin):
    def __init__(self, user):
        self.username = user.get("name")
        self.password_hash = user.get("password")
        self.id = user.get("id")

    @staticmethod
    def queryUser(username):
        for user in USERS:
            if (user.get('name') == username):
                return User(user)
        return None

    def verifyPassword(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id

    def get(user_id):
        if not user_id:
            return None
        for user in USERS:
            if str(user.get('id')) == str(user_id):
                return User(user)
        print('None')
        return None