# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Index, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


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
    status = db.Column(db.ENUM('WAITING', 'EXPIRED_VBANK', 'CHARGED', 'EXPIRED', 'CANCELED'), server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime)

    payment_method = db.relationship('PaymentMethod', primaryjoin='Payment.method_code == PaymentMethod.code', backref='payments')
    payment_module = db.relationship('PaymentModule', primaryjoin='Payment.module_code == PaymentModule.code', backref='payments')
    user = db.relationship('User', primaryjoin='Payment.user_id == User.id', backref='payments')


class PaymentsLg(Payment):
    __tablename__ = 'payments_lg'

    payment_id = db.Column(db.ForeignKey('payments.id'), primary_key=True)
    TID = db.Column(db.String(24, 'utf8_unicode_ci'), nullable=False, index=True)
    lg_order_id = db.Column(db.String(40, 'utf8_unicode_ci'), nullable=False)
    hash_data = db.Column(db.String(255, 'utf8_unicode_ci'), nullable=False)
    finance_name = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)
    finance_code = db.Column(db.String(10, 'utf8_unicode_ci'), nullable=False)
    finance_auth_num = db.Column(db.String(20, 'utf8_unicode_ci'))
    cash_receipt_self = db.Column(db.ENUM('Y', 'N'), nullable=False, server_default=db.FetchedValue())
    cash_receipt_num = db.Column(db.String(10, 'utf8_unicode_ci'), nullable=False)
    pcancel_flag = db.Column(db.ENUM('0', '1'), nullable=False, server_default=db.FetchedValue())
    account_num = db.Column(db.String(20, 'utf8_unicode_ci'))
    cash_seq_no = db.Column(db.String(3, 'utf8_general_ci'))
    account_owner = db.Column(db.String(40, 'utf8_unicode_ci'))
    account_payer = db.Column(db.String(40, 'utf8_unicode_ci'))
    cash_flag = db.Column(db.ENUM('N', 'R', 'I', 'C'), nullable=False, server_default=db.FetchedValue())
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
