# TODO Salary details having employee id, current salary

import datetime

import sqlalchemy
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class Salary(SqlAlchemyBase):
    __tablename__ = 'salary'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    designation = sqlalchemy.Column(sqlalchemy.String)
    street = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String, index=True)
    state = sqlalchemy.Column(sqlalchemy.String, index=True)
    gross_salary = sqlalchemy.Column(sqlalchemy.Integer)
    deductions = sqlalchemy.Column(sqlalchemy.Integer)
    net_salary = sqlalchemy.Column(sqlalchemy.Integer)

    # max_storage = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    employee_id = orm.relation('Employee', back_populates='employee_id')