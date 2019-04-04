from flask import Flask
from . import models, routes
from .config import config_by_name

def create_app(args):
    app = Flask(__name__)
    app.config.from_object(config_by_name[args.env or 'dev'])
    if 'SQLALCHEMY_DATABASE_URI' not in app.config:
        app.config['SQLALCHEMY_DATABASE_URI'] = args.db
    models.init_app(app)
    routes.init_app(app)
    return app