# TODO Employee list to be maintained having id, name, designation, experience

import datetime

import sqlalchemy
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class employees(SqlAlchemyBase):
    __tablename__ = 'employees'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    employee_id = sqlalchemy.Column(sqlalchemy.Integer, index=True, autoincrement=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    designation = sqlalchemy.Column(sqlalchemy.String)
    street = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String, index=True)
    state = sqlalchemy.Column(sqlalchemy.String, index=True)

    #max_storage = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    #scooters = orm.relation('Scooter', back_populates='location')