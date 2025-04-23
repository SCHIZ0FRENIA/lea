from flask import current_app, g, app
from pymongo import MongoClient


def get_db():
    """Connects to the db"""
    if 'db' not in g:
        try:
            mongo_uri = current_app.config['MONGO_URI']
            db_name = current_app.config['DB_NAME']
            g.client = MongoClient(mongo_uri)
            g.client.admin.command('ping')
            g.db = g.client[db_name]
            print("Connected to MongoDB")
        except Exception as e:
            print(f"Could not connect to MONGO. Exception: {e}")
            g.db = None
    return g.db

def get_users_collection():
    """Gets user collection from db"""
    db = get_db()
    if db:
        return db[current_app.config['USERS_COLLECTION_NAME']]
    return None

def close_db():
    client = g.pop('client', None)
    if client is not None:
        client.close()
        print("Mongo db connection closed.")
    g.pop('db', None)
