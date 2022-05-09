from flask import render_template,request,flash,redirect,url_for
from . import auth
from .. import db
from flask_login import login_user,login_required,logout_user,current_user

from ..models import User
from werkzeug.security import generate_password_hash,check_password_hash

  

@auth.route('/login',methods = ["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully!', category='success')
                login_user(user,remember=True)
                return redirect(url_for('main.home'))
                
            else:
                flash('Incorrect password or email address! Try again.',category='error')
                
        else:
            flash('Email does not exist',category='error')
    return render_template("auth/login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods = ["GET","POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username  = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', category='error')
        
        elif len(email) < 4:
            flash('Email must be greater than three characters!',category='error')
        elif len(username) < 2:
            flash('Name must be greater than one characters!',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!',category='error')
        elif len(password1) < 7:
            flash('Password must be atleast seven characters!',category='error')
        else:
            new_user = User(email = email,username=username,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!',category='success')
            login_user(user,remember=True)
            return redirect(url_for('auth.login'))
    return render_template("auth/sign_up.html")
