import os
import sys
from flask import send_file
from flask import Flask, session, render_template, request, redirect, url_for, flash, jsonify
from flask_bcrypt import Bcrypt
from flask_session import Session
from database import Base,Accounts,Customers,Users
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = os.urandom(24)

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Set up database
engine = create_engine('sqlite:///database.db',connect_args={'check_same_thread': False},echo=True)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))
@app.route("/")
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    
    return render_template("login.html" , login=True)
    
# MAIN
@app.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    else:
        return render_template("home.html" , home=True)

@app.route("/addcustomer")
def addcustomer():
    if 'user' not in session:
        if session['usert']=="executive":
            if request.method == "POST":
                cust_id = request.form.get("username").upper()
                name = request.form.get("name")
                address = request.form.get("address")
                age= request.form.get("age")
                state = request.form.get("state")
                city = request.form.get("city")
                db.execute("INSERT INTO customers (cust_id,name,address,age,state,city) VALUES (:c,:n,:add,:a,:s,:city)", {"c": cust_id,"n":name,"add":address,"a": age,"s":state,"city":city})
                db.commit()
                return redirect(url_for('dashboard'))
    return render_template('addcustomer.html', addcustomer=True)

# # Change Pasword
# @app.route("/change-password", methods=["GET", "POST"])
# def changepass():
#     if 'user' not in session:
#         return redirect(url_for('login'))
#     msg=""
#     if request.method == "POST":
#         try:
#             epswd = request.form.get("epassword")
#             cpswd = request.form.get("cpassword")
#             passw_hash = bcrypt.generate_password_hash(cpswd).decode('utf-8')
#             exist=db.execute("SELECT password FROM accounts WHERE id = :u", {"u": session['user']}).fetchone()
#             if bcrypt.check_password_hash(exist['password'], epswd) is True:
#                 res=db.execute("UPDATE accounts SET password = :u WHERE id = :v",{"u":passw_hash,"v":session['user']})
#                 db.commit()
#                 if res.rowcount > 0:
#                     return redirect(url_for('dashboard'))
#         except exc.IntegrityError:
#             msg = "Unable to process try again"
#     msg="Existing Not matching"
#     return render_template("change_password.html",m=msg)

# # Reset
# @app.route("/reset", methods=["GET", "POST"])
# def reset():
#     msg=""
#     if session['usert']=="admin":
        
#         if request.method == "POST":
#             rollno = request.form.get("rollno")
#             passw_hash = bcrypt.generate_password_hash("srit").decode('utf-8')
#             res=db.execute("UPDATE accounts SET password = :u WHERE id = :v",{"u":passw_hash,"v":rollno})
#             db.commit()
#             if res is not None:
#                 return redirect(url_for('dashboard'))
#         msg=""
#         return render_template("pswdreset.html",m=msg)
#     else:
#         return redirect(url_for('dashboard'))
# LOGOUT
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))
# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == "POST":
        usern = request.form.get("username").upper()
        passw = request.form.get("password").encode('utf-8')
        result = db.execute("SELECT * FROM users WHERE id = :u", {"u": usern}).fetchone()
        if result is not None:
            print(result['password'])
            if bcrypt.check_password_hash(result['password'], passw) is True:
                session['user'] = usern
                session['namet'] = result.name
                session['usert'] = result.user_type
                return redirect(url_for('dashboard'))
        flash("Username or password is incorrect.")
    return render_template("login.html", login=True)
# Main
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
