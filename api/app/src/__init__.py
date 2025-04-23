from flask import Flask, app
from .auth.auth_bp import auth_bp
from .config import Config
from .database.database import close_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth_bp)

    return app

@app.appcontext_tearing_down
def close_connection():
    """Closes the connection """
    close_db()