from ..models.models import db, Member
from flask import jsonify

def init_app(app):
    @app.route("/members/<int:user_id>/")
    def getMember(user_id):
        return jsonify(Member.query.filter_by(USERID=user_id).first().as_dict())

    @app.route("/members/<int:user_id>/", methods=['POST'])
    def updateMember(user_id):
        member = Member.query.filter_by(USERID=user_id).first()

        if member.online == '1':
            member.online = '0'
        else:
            member.online = '1'

        db.session.commit()
        return jsonify(
            result=member.online
        )