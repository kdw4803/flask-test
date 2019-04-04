from ..models.models import db, Order
from flask import jsonify

def init_app(app):
    @app.route("/orders/<int:OID>/")
    def getOrder(OID):
        order = Order.query.filter_by(OID=OID).first()

        if order is not None:
            return jsonify(order.as_dict())
        else:
            return jsonify({})

    @app.route('/orders', methods=['POST'])
    def createOrder():
        order = Order()
        db.session.add(order)
        db.session.commit()

        return jsonify(order.as_dict())

    @app.route("/orders/<int:OID>/", methods=['PUT'])
    def updateOrder(OID):
        order = Order.query.filter_by(OID=OID).first()

        if order.status == 'ONGOING':
            order.status = 'COMPLETED'
        else:
            order.status = 'ONGOING'

        db.session.commit()
        return jsonify(order.as_dict())