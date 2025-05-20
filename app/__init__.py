from flask import Flask
from .extensions import initialize_extensions, mongo
import os

from .services.public_decks_service import PublicDecksService
from .services.user_service import UserService
from .static.services import Services


class Config:
    DEBUG = os.getenv("DEBUG", True)
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:5000/lea")
    SECRET_KEY = os.getenv("SECRET_KEY", "JKSDHVUPINJEWIUVH:DSNVBOKKJ!@#J!@#()IJFDNSNV*#(@RHFVJDN(*#EINDV)#@()IFJIVDSO")

def create_app():
    """Generates server"""

    app = Flask(__name__)
    app.config.from_object(Config)

    initialize_extensions(app)

    from .routes.auth_route import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/v1/auth')

    from .routes.public_decks_route import public_decks_bp
    app.register_blueprint(public_decks_bp, url_prefix='/v1/decks')

    @app.route('/')
    def health_check():
        return 'server is ok'

    with app.app_context():
        app.services = {
            Services.USER_SERVICE: UserService(mongo.db),
            Services.PUBLIC_DECKS_SERVICE: PublicDecksService(mongo.db)
        }

    return app
