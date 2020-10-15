from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from app import models, routes
from app.main.config import config_by_name


db = SQLAlchemy()


def create_app(config_name):
    """Create flak app  with a enviroment"""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    return app
