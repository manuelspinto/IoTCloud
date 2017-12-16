"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask_login import login_required, login_user, logout_user 
from flask_wtf import FlaskForm
from IoTCloud import app

@app.route('/')
@app.route('/home')
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


#def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
 #   form = LoginForm()
  #  if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
   #     login_user(user)

    #    flask.flash('Logged in successfully.')

     #   next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
      #  if not is_safe_url(next):
       #     return flask.abort(400)

        #return flask.redirect(next or flask.url_for('index'))
    #return flask.render_template('login.html', form=form)

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
    return redirect(url_for('index'))

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
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))