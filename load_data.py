import sys
import csv
import os
from database import Base,Accounts,Customers,Users,CustomerLog,Transactions
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bcrypt import Bcrypt
from flask import Flask
app = Flask(__name__)
engine = create_engine('sqlite:///database.db',connect_args={'check_same_thread': False},echo=True)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))
bcrypt = Bcrypt(app)


def accounts():
    usern = 'C00000001'
    name = 'ramesh'
    usert = 'executive'
    passw = 'Ramesh@001'
    passw_hash = bcrypt.generate_password_hash(passw).decode('utf-8')
    db.execute("INSERT INTO users (id,name,user_type,password) VALUES (:u,:n,:t,:p)", {"u": usern,"n":name,"t":usert ,"p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")
    usern = 'C00000002'
    name = 'suresh'
    usert = 'cashier'
    passw = 'Suresh@002'
    passw_hash = bcrypt.generate_password_hash(passw).decode('utf-8')
    db.execute("INSERT INTO users (id,name,user_type,password) VALUES (:u,:n,:t,:p)", {"u": usern,"n":name,"t":usert ,"p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")
    usern = 'C00000003'
    name = 'mahesh'
    usert = 'teller'
    passw = 'Mahesh@003'
    passw_hash = bcrypt.generate_password_hash(passw).decode('utf-8')
    db.execute("INSERT INTO users (id,name,user_type,password) VALUES (:u,:n,:t,:p)", {"u": usern,"n":name,"t":usert ,"p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")

if __name__ == "__main__":
    accounts()