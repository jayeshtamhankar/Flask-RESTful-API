from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .config import Config

database = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    database.init_app(app)
    CORS(app)

    from .routes import api_routes
    app.register_blueprint(api_routes, url_prefix='/api')

    return app