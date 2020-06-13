import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String(250),nullable=False)
    user_type = Column(String(250), nullable=False)
    password = Column(String(250))
class Customers(Base):
    __tablename__='customers'
    cust_id = Column(String, primary_key=True)
    name = Column(String(250),nullable=False)
    address = Column(String(250), nullable=False)
    age = Column(Integer)
    state = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
class Accounts(Base):
    __tablename__='accounts'
    cust_id = Column(String, primary_key=True)
    acc_id = Column(String(250),nullable=False)
    acc_type = Column(String(250),nullable=False)
    balance = Column(Integer, nullable=False)
    c_id = Column(String, ForeignKey('customers.cust_id'))
    customers = relationship(Customers)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)