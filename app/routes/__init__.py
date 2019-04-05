from . import base, payments, users

def init_app(app):
    base.init_app(app)
    # 기존 db
    # members.init_app(app)
    # orders.init_app(app)

    # billing db
    payments.init_app(app)
    users.init_app(app)
