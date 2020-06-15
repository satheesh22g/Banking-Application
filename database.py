import os
import sys ,datetime
from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger
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
    cust_id = Column(Integer, primary_key=True, autoincrement=True)
    cust_ssn_id = Column(Integer, unique=True)
    name = Column(String(250),nullable=False)
    address = Column(String(250), nullable=False)
    age = Column(Integer)
    state = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)

class CustomerLog(Base):
    __tablename__='customerlog'
    log_id = Column(Integer, primary_key=True, autoincrement=True)
    cust_id = Column(Integer, ForeignKey('customers.cust_id'))
    log_message = Column(String(250), nullable=False)
    time_stamp = Column(DateTime(timezone=False), default=datetime.datetime.utcnow)

class Accounts(Base):
    __tablename__='accounts'
    acc_id = Column(Integer,primary_key=True,autoincrement=True)
    acc_type = Column(String(250),nullable=False)
    balance = Column(Integer, nullable=False)
    cust_id = Column(Integer, ForeignKey('customers.cust_id'))
    status = Column(String(250), nullable=False)
    customers = relationship(Customers)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)