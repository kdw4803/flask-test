from flask import Flask
from . import models, routes
from .config import config_by_name

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    models.init_app(app)
    routes.init_app(app)
    return app