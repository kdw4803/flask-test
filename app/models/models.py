# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, JSON, Numeric, SmallInteger, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    __tablename__ = 'members'

    USERID = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True, server_default=db.FetchedValue())
    username = db.Column(db.String(80), nullable=False, unique=True, server_default=db.FetchedValue())
    password = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue())
    funds = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    afunds = db.Column(db.BigInteger, nullable=False)
    withdrawn = db.Column(db.BigInteger, nullable=False)
    used = db.Column(db.BigInteger, nullable=False)
    fullname = db.Column(db.String(100), nullable=False, index=True, server_default=db.FetchedValue())
    addtime = db.Column(db.String(20), nullable=False, index=True, server_default=db.FetchedValue())
    profilepicture = db.Column(db.String(100), server_default=db.FetchedValue())
    lastlogin = db.Column(db.String(20), nullable=False, index=True, server_default=db.FetchedValue())
    online = db.Column(ENUM('1', '0'), index=True, server_default=db.FetchedValue())
    vacation = db.Column(ENUM('ACTIVE', 'EXPIRE', 'INACTIVE'), nullable=False, index=True, server_default=db.FetchedValue())
    remember_token = db.Column(db.String(100))
    ip = db.Column(db.String(20), nullable=False)
    lip = db.Column(db.String(20), nullable=False)
    mobile = db.Column(db.String(20), index=True)
    contact_number = db.Column(db.String(20, 'utf8_bin'))
    open_mobile = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    canceled = db.Column(db.Integer, server_default=db.FetchedValue())
    completed = db.Column(db.Integer, server_default=db.FetchedValue())
    rev = db.Column(db.Integer)
    mobile_on = db.Column(ENUM('1', '0'), server_default=db.FetchedValue())
    warning = db.Column(db.Integer, server_default=db.FetchedValue())
    memo = db.Column(db.Text)
    penalty = db.Column(db.Integer, server_default=db.FetchedValue())
    grade = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
    rating = db.Column(ENUM('NEW', 'JUNIOR', 'SENIOR', 'SEMIPRO', 'PRO', 'MASTER'), index=True, server_default=db.FetchedValue())
    mail_settings = db.Column(db.Text)
    birthday = db.Column(db.String(10), server_default=db.FetchedValue())
    gender = db.Column(db.String(1))
    av_time_from = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    av_time_to = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    avg_response_rate = db.Column(db.Integer, server_default=db.FetchedValue())
    avg_response_time = db.Column(db.Integer, server_default=db.FetchedValue())
    success_rate_sell = db.Column(db.Float, server_default=db.FetchedValue())
    success_rate_buy = db.Column(db.Float, server_default=db.FetchedValue())
    api_token = db.Column(db.String(96), index=True)
    facebook_id = db.Column(db.String(128), index=True)
    google_id = db.Column(db.String(128))
    naver_id = db.Column(db.String(128), index=True)
    kakao_id = db.Column(db.String(128), index=True)
    conn_info_id = db.Column(db.String(100), index=True)
    dupl_info_id = db.Column(db.String(100))
    acquisition = db.Column(db.String(40))

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
