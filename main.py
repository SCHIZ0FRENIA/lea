import os

from app import create_app

os.environ["UV_ENV_FILE"] = ".venv/.env"

app = create_app()

if __name__ == '__main__':
    host = os.environ.get('FLASK_RUN_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_RUN_PORT', 3000))
    app.run(host=host, port=port)