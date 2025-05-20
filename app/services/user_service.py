from ..utils.exceptions.database_exception import DatabaseException
from ..utils.hash import hash_password, check_password


class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, login, password, role):
        result = self.db.users.insert_one({
            "login": login,
            "password": hash_password(password),
            "role": role
        })

        return result

    def check_user(self, login, password):
        result = self.db.users.find_one({
            "login": login
        })

        if result is None:
            raise DatabaseException("No such user.")

        if check_password(result["password"], password):
            return result
        else:
            raise DatabaseException("Password is incorrect")