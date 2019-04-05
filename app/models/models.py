# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, JSON, Numeric, SmallInteger, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class PaymentMethod(db.Model):
    __tablename__ = 'payment_methods'

    code = db.Column(db.String(100, 'utf8_unicode_ci'), primary_key=True)
    name = db.Column(db.String(100, 'utf8_unicode_ci'))
    order = db.Column(db.Integer, server_default=db.FetchedValue())
    status = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime)


class PaymentModule(db.Model):
    __tablename__ = 'payment_modules'

    code = db.Column(db.String(100, 'utf8_unicode_ci'), primary_key=True)
    name = db.Column(db.String(100, 'utf8_unicode_ci'))
    order = db.Column(db.Integer, server_default=db.FetchedValue())
    status = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime)


class Payment(db.Model):
    __tablename__ = 'payments'
    __table_args__ = (
        db.Index('parent_id_index', 'id', 'parent_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    parent_id = db.Column(db.BigInteger, nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False, index=True)
    module_code = db.Column(db.ForeignKey('payment_modules.code'), nullable=False, index=True)
    method_code = db.Column(db.ForeignKey('payment_methods.code'), nullable=False, index=True)
    status = db.Column(ENUM('WAITING', 'EXPIRED_VBANK', 'CHARGED', 'EXPIRED', 'CANCELED'), server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime)

    payment_method = db.relationship('PaymentMethod', primaryjoin='Payment.method_code == PaymentMethod.code', backref='payments')
    payment_module = db.relationship('PaymentModule', primaryjoin='Payment.module_code == PaymentModule.code', backref='payments')
    user = db.relationship('User', primaryjoin='Payment.user_id == User.id', backref='payments')

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class PaymentsLg(Payment):
    __tablename__ = 'payments_lg'

    payment_id = db.Column(db.ForeignKey('payments.id'), primary_key=True)
    TID = db.Column(db.String(24, 'utf8_unicode_ci'), nullable=False, index=True)
    lg_order_id = db.Column(db.String(40, 'utf8_unicode_ci'), nullable=False)
    hash_data = db.Column(db.String(255, 'utf8_unicode_ci'), nullable=False)
    finance_name = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)
    finance_code = db.Column(db.String(10, 'utf8_unicode_ci'), nullable=False)
    finance_auth_num = db.Column(db.String(20, 'utf8_unicode_ci'))
    cash_receipt_self = db.Column(ENUM('Y', 'N'), nullable=False, server_default=db.FetchedValue())
    cash_receipt_num = db.Column(db.String(10, 'utf8_unicode_ci'), nullable=False)
    pcancel_flag = db.Column(ENUM('0', '1'), nullable=False, server_default=db.FetchedValue())
    account_num = db.Column(db.String(20, 'utf8_unicode_ci'))
    cash_seq_no = db.Column(db.String(3, 'utf8_general_ci'))
    account_owner = db.Column(db.String(40, 'utf8_unicode_ci'))
    account_payer = db.Column(db.String(40, 'utf8_unicode_ci'))
    cash_flag = db.Column(ENUM('N', 'R', 'I', 'C'), nullable=False, server_default=db.FetchedValue())
    cash_total_amount = db.Column(db.Integer)
    cash_current_amount = db.Column(db.Integer)
    sa_owner = db.Column(db.String(10, 'utf8_unicode_ci'))
    response_code = db.Column(db.String(10, 'utf8_unicode_ci'))
    response_message = db.Column(db.Text(collation='utf8_unicode_ci'))
    requested_at = db.Column(db.DateTime)
    paid_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    cash = db.Column(db.BigInteger, nullable=False)
    profits = db.Column(db.BigInteger, nullable=False)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}



# 기존 db

# class Member(db.Model):
#     __tablename__ = 'members'

#     USERID = db.Column(db.BigInteger, primary_key=True)
#     email = db.Column(db.String(80), nullable=False, unique=True, server_default=db.FetchedValue())
#     username = db.Column(db.String(80), nullable=False, unique=True, server_default=db.FetchedValue())
#     password = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue())
#     funds = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
#     afunds = db.Column(db.BigInteger, nullable=False)
#     withdrawn = db.Column(db.BigInteger, nullable=False)
#     used = db.Column(db.BigInteger, nullable=False)
#     fullname = db.Column(db.String(100), nullable=False, index=True, server_default=db.FetchedValue())
#     addtime = db.Column(db.String(20), nullable=False, index=True, server_default=db.FetchedValue())
#     profilepicture = db.Column(db.String(100), server_default=db.FetchedValue())
#     lastlogin = db.Column(db.String(20), nullable=False, index=True, server_default=db.FetchedValue())
#     online = db.Column(ENUM('1', '0'), index=True, server_default=db.FetchedValue())
#     vacation = db.Column(ENUM('ACTIVE', 'EXPIRE', 'INACTIVE'), nullable=False, index=True, server_default=db.FetchedValue())
#     remember_token = db.Column(db.String(100))
#     ip = db.Column(db.String(20), nullable=False)
#     lip = db.Column(db.String(20), nullable=False)
#     mobile = db.Column(db.String(20), index=True)
#     contact_number = db.Column(db.String(20, 'utf8_bin'))
#     open_mobile = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
#     canceled = db.Column(db.Integer, server_default=db.FetchedValue())
#     completed = db.Column(db.Integer, server_default=db.FetchedValue())
#     rev = db.Column(db.Integer)
#     mobile_on = db.Column(ENUM('1', '0'), server_default=db.FetchedValue())
#     warning = db.Column(db.Integer, server_default=db.FetchedValue())
#     memo = db.Column(db.Text)
#     penalty = db.Column(db.Integer, server_default=db.FetchedValue())
#     grade = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
#     rating = db.Column(ENUM('NEW', 'JUNIOR', 'SENIOR', 'SEMIPRO', 'PRO', 'MASTER'), index=True, server_default=db.FetchedValue())
#     mail_settings = db.Column(db.Text)
#     birthday = db.Column(db.String(10), server_default=db.FetchedValue())
#     gender = db.Column(db.String(1))
#     av_time_from = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
#     av_time_to = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
#     avg_response_rate = db.Column(db.Integer, server_default=db.FetchedValue())
#     avg_response_time = db.Column(db.Integer, server_default=db.FetchedValue())
#     success_rate_sell = db.Column(db.Float, server_default=db.FetchedValue())
#     success_rate_buy = db.Column(db.Float, server_default=db.FetchedValue())
#     api_token = db.Column(db.String(96), index=True)
#     facebook_id = db.Column(db.String(128), index=True)
#     google_id = db.Column(db.String(128))
#     naver_id = db.Column(db.String(128), index=True)
#     kakao_id = db.Column(db.String(128), index=True)
#     conn_info_id = db.Column(db.String(100), index=True)
#     dupl_info_id = db.Column(db.String(100))
#     acquisition = db.Column(db.String(40))

#     def as_dict(self):
#         return {x.name: getattr(self, x.name) for x in self.__table__.columns}

# class Order(db.Model):
#     __tablename__ = 'orders'
#     __table_args__ = (
#         db.Index('buyer_USERID', 'buyer_USERID', 'status'),
#         db.Index('type_id_2', 'type_id', 'status'),
#         db.Index('seller_USERID_2', 'seller_USERID', 'status'),
#         db.Index('type_2', 'type', 'type_id'),
#         db.Index('PID_2', 'PID', 'status')
#     )

#     OID = db.Column(db.BigInteger, primary_key=True)
#     DOID = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue())
#     buyer_USERID = db.Column(db.BigInteger, index=True)
#     seller_USERID = db.Column(db.BigInteger, index=True)
#     type = db.Column(ENUM('GIG', 'GIG_REQUEST', 'INBOX_REQUEST', 'CUSTOM_QUOTE', 'CALLING'), nullable=False, index=True, server_default=db.FetchedValue())
#     type_id = db.Column(db.BigInteger, index=True)
#     # PLID = db.Column(db.ForeignKey('posts_log.PLID'), index=True)
#     package_id = db.Column(db.BigInteger, index=True)
#     PID = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
#     status = db.Column(ENUM('READYORDER', 'ONGOING', 'TROUBLESHOOTING', 'DELIVERED', 'COMPLETED', 'CANCELEDBYBUYER', 'CANCELEDBYSELLER'), nullable=False, index=True, server_default=db.FetchedValue())
#     total_price = db.Column(db.BigInteger)
#     price = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
#     total_days = db.Column(db.BigInteger)
#     extra_data = db.Column(db.Text)
#     quantity = db.Column(db.Integer, server_default=db.FetchedValue())
#     days = db.Column(db.BigInteger)
#     agreed = db.Column(db.Integer, server_default=db.FetchedValue())
#     isDirect = db.Column(db.Integer, server_default=db.FetchedValue())
#     created_at = db.Column(db.DateTime, index=True, server_default=db.FetchedValue())
#     updated_at = db.Column(db.DateTime, server_default=db.FetchedValue())
#     started_at = db.Column(db.DateTime, index=True)
#     expected_completed_at = db.Column(db.DateTime)
#     delivered_at = db.Column(db.DateTime, index=True)
#     completed_at = db.Column(db.DateTime, index=True)

#     # posts_log = db.relationship('PostsLog', primaryjoin='Order.PLID == PostsLog.PLID', backref='orders')

#     def as_dict(self):
#         return {x.name: getattr(self, x.name) for x in self.__table__.columns}