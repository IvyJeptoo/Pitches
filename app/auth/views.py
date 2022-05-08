from flask import render_template,request,flash
from . import auth

@auth.route('/login',methods = ["GET","POST"])
def login():
    return render_template("auth/login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up',methods = ["GET","POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName  = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than three characters!',category='error')
        elif len(firstName) < 2:
            flash('Name must be greater than one characters!',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!',category='error')
        elif len(password1) < 7:
            flash('Password must be atleast seven characters!',category='error')
        else:
            #add user to db
            flash('Account created successfully!',category='success')
    return render_template("auth/sign_up.html")
