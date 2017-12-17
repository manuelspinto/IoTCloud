"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash, url_for, redirect, render_template, abort ,g
from flask_login import login_required, login_user, logout_user , login_manager, current_user
from flask_wtf import FlaskForm
from IoTCloud import app, login_manager
from IoTCloud.dbm.dbdeployer import Deploy
from IoTCloud.dbm.models import User
from IoTCloud.dbm.rdb import db

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/iotcloud')
def iotcloud():
    """Renders test page"""
    return render_template(
        'iotcloud.html',
        title='IoTCloud',
        year=datetime.now().year,
        message='Test page'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
        
@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))
 

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
 
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember = remember_me)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('home'))

@app.route('/admin')
@login_required
def admin():
    """Renders the about page."""
    return render_template(
        'admin.html',
        title='Admin Page',
        year=datetime.now().year,
        message='Welcome to the admin page'
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))