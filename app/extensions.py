import logging
from logging.handlers import RotatingFileHandler

from flask_pymongo import PyMongo

mongo = PyMongo()

def initialize_extensions(app):
    """
    Initializes all extensions that are used in this app
    """

    # mongo init
    mongo.init_app(app)
    mongo.db.users.create_index("name", unique = True)


    # Configure logger
    handler = RotatingFileHandler(
        'app.log', maxBytes=10000, backupCount=3
    )
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)