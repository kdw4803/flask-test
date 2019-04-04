from flask import Flask
from . import base, members, orders

def init_app(app):
    base.init_app(app)
    members.init_app(app)
    orders.init_app(app)