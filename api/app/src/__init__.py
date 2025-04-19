from flask import Flask
from flask_pymongo import PyMongo
from .auth.auth_bp import auth_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth_bp)

    return app