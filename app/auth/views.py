from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template("auth/login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("auth/sign_up.html")
