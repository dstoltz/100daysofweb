# TODO Employee list to be maintained having id, name, designation, experience

import datetime

import sqlalchemy
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class Employee(SqlAlchemyBase):
    __tablename__ = 'employee'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    employee_id = sqlalchemy.Column(sqlalchemy.Integer, index=True, autoincrement=True, unique=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    designation = sqlalchemy.Column(sqlalchemy.String)
    street = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String, index=True)
    state = sqlalchemy.Column(sqlalchemy.String, index=True)

    #max_storage = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    #gross_salary = orm.relation('Salary', back_populates='gross_salary')