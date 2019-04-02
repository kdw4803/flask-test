from flask import Flask
from . import models, routes
from .config import config_by_name

def create_app(config_name, db):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = db
    models.init_app(app)
    routes.init_app(app)
    return app