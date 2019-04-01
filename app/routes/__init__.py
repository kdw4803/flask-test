from flask import Flask
from . import base, members

def init_app(app):
    base.init_app(app)
    members.init_app(app)