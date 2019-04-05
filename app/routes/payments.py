from ..models.models import db, Payment
from flask import jsonify

def init_app(app):
    @app.route("/payments/<int:id>/")
    def getPayment(id):
        payment = Payment.query.filter_by(id=id).first()

        if payment is not None:
            return jsonify(payment.as_dict())
        else:
            return jsonify({})

    @app.route('/payments', methods=['POST'])
    def createPayment():
        payment = Payment(parent_id=0, user_id=1, module_code='LG', method_code='CARD')
        db.session.add(payment)
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

        return jsonify(payment.as_dict())

    @app.route("/payments/<int:id>/", methods=['PUT'])
    def updatePayment(id):
        payment = Payment.query.filter_by(id=id).first()

        if payment.status == 'WAITING':
            payment.status = 'CHARGED'
        else:
            payment.status = 'WAITING'

        db.session.commit()
        return jsonify(payment.as_dict())