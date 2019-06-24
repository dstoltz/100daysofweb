# TODO Salary in hand details having employee id, CTC salary, pf deduction or any other deduction and net salary to be given and also maintain  details of total savings of employee

import datetime

import sqlalchemy
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class Salary_In_Hand(SqlAlchemyBase):
    __tablename__ = 'salary_in_hand'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    designation = sqlalchemy.Column(sqlalchemy.String)
    

    

    employee = orm.relation('Employee', back_populates='salary_in_hand')