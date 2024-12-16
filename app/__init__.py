from flask import Flask
from .config import DevelopmentConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    from .routes import register_blueprints
    register_blueprints(app)

    return app