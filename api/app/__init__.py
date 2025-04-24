from flask import Flask
from .extensions import initialize_extensions
import os

class Config:
    DEBUG = os.getenv("DEBUG", True)
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:5000/")
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

def create_app():
    """Generates server"""

    app = Flask(__name__)
    app.config.from_object(Config)

    initialize_extensions(app)

    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/v1/users')

    @app.route('/')
    def health_check():
        return 'server is ok'

    return app
