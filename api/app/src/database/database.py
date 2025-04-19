from pymongo import MongoClient

from api.app.src import constants


class Database:
    def __init__(self):
        try:
            self.client = MongoClient(constants.connection_string)
            self.client.admin.command('ping')
            self.db = self.client[constants.db_name]
            self.users_db = self.db[constants.users_db_name]
            print("Successfully connected to MongoDB!")
        except Exception as e:
            print(f"Could not connect to MongoDB: {e}")


    def add_user(self, name, password):
        if self.users_db.find_one({"name" : name}):
            return False
        else:
            self.users_db.insert_one({
                "name": name,
                "password": password
            })
            return True

instance = Database()
