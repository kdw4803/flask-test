from ..models.models import db, User
from flask import jsonify

def init_app(app):
    @app.route("/users/<int:id>/")
    def getUser(id):
        user = User.query.filter_by(id=id).first()

        if user is not None:
            return jsonify(user.as_dict())
        else:
            return jsonify({})

    @app.route('/users', methods=['POST'])
    def createUser():
        user = User(cash=0, profits=0)
        db.session.add(user)
        db.session.commit()

        # id = db.Column(db.BigInteger, primary_key=True)
        # parent_id = db.Column(db.BigInteger, nullable=False)
        # user_id = db.Column(db.ForeignKey('users.id'), nullable=False, index=True)
        # module_code = db.Column(db.ForeignKey('payment_modules.code'), nullable=False, index=True)
        # method_code = db.Column(db.ForeignKey('payment_methods.code'), nullable=False, index=True)
        # status = db.Column(ENUM('WAITING', 'EXPIRED_VBANK', 'CHARGED', 'EXPIRED', 'CANCELED'), server_default=db.FetchedValue())
        # amount = db.Column(db.BigInteger, server_default=db.FetchedValue())
        # created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
        # updated_at = db.Column(db.DateTime)

        # payment_method = db.relationship('PaymentMethod', primaryjoin='Payment.method_code == PaymentMethod.code', backref='payments')
        # payment_module = db.relationship('PaymentModule', primaryjoin='Payment.module_code == PaymentModule.code', backref='payments')
        # user = db.relationship('User', primaryjoin='Payment.user_id == User.id', backref='payments')

        return jsonify(user.as_dict())

    @app.route("/users/<int:id>/", methods=['PUT'])
    def updateUsers(id):
        user = User.query.filter_by(id=id).first()

        user.cash += 100
        user.profits += 100

        db.session.commit()
        return jsonify(user.as_dict())