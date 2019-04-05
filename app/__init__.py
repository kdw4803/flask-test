from flask import Flask
from . import models, routes
from .config import config_by_name

app = Flask(__name__)

def create_app(args):
    app.config.from_object(config_by_name['dev'])

    if args.env != None:
        app.config.from_object(config_by_name[args.env])
    else:
        app.config.from_object(config_by_name['dev'])
        
    if args.db != None:
        app.config['SQLALCHEMY_DATABASE_URI'] = args.db

    models.init_app(app)
    routes.init_app(app)
    return app