from flask_pymongo import PyMongo

mongo = PyMongo()

def initialize_extensions(app):
    """
    Initializes all extensions that are used in this app
    """

    mongo.init_app(app)