from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import SignUpForm, LoginForm
from .. import db
from ..models import User
from ..email import mail_message


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Welcome to Pitch", "email/welcome", user.email, user=user)
        
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/signup.html', signupform=form, title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(username=login.username.data).first()
        if user is not None and user.verify_password(login.password.data):
            login_user(user, login.rememberMe.data)
            return redirect(url_for('main.index'))

        flash('Invalid username or password')

    title = 'Login'

    return render_template('auth/login.html', loginform=login, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
# from flask import render_template,request,flash,redirect,url_for
# from . import auth
# from .. import db
# from flask_login import login_user,login_required,logout_user,current_user
# from ..models import User
# from werkzeug.security import generate_password_hash,check_password_hash

  

# @auth.route('/login',methods = ["GET","POST"])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password,password):
#                 flash('Logged in successfully!', category='success')
#                 login_user(user,remember=True)
#                 return redirect(url_for('main.home'))
                
#             else:
#                 flash('Incorrect password or email address! Try again.',category='error')
                
#         else:
#             flash('Email does not exist',category='error')
#     return render_template("auth/login.html",user=current_user)

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))

# @auth.route('/sign-up',methods = ["GET","POST"])
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         username  = request.form.get('username')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')
        
#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email already exists!', category='error')
        
#         elif len(email) < 4:
#             flash('Email must be greater than three characters!',category='error')
#         elif len(username) < 2:
#             flash('Name must be greater than one characters!',category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match!',category='error')
#         elif len(password1) < 7:
#             flash('Password must be atleast seven characters!',category='error')
#         else:
#             new_user = User(email = email,username=username,password=generate_password_hash(password1,method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Account created successfully!',category='success')
#             login_user(user,remember=True)
#             return redirect(url_for('auth.login'))
#     return render_template("auth/sign_up.html", user=current_user)
