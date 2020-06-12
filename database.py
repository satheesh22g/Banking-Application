import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Accounts(Base):
    __tablename__ = 'accounts'
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


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)