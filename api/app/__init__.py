from flask import Flask
from .extensions import initialize_extensions
import os

class Config:
    DEBUG = os.getenv("DEBUG", True)
    MONGO_URI = os.getenv("MONGO_URI", "Add .env file")
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

def create_app():
    """Generates server"""

    app = Flask(__name__)

    initialize_extensions(app)
