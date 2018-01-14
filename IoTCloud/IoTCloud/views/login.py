from . import *

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')

	username = request.form['username']
	password = request.form['password']
	remember_me = False
	if 'remember_me' in request.form:
		remember_me = True
	registered_user = User.query.filter_by(username=username).first()
	db.session.close()

	login_fail = False
	if registered_user is None:
		login_fail = True
	else:
		hashed_pw = registered_user.password
		if not bcrypt.checkpw(password.encode('utf-8'),hashed_pw.encode('utf-8')):
			login_fail = True
	if login_fail:
		flash('Username or Password is invalid' , 'danger')
		return redirect(url_for('login'))
	
	login_user(registered_user, remember = remember_me)
	flash('Logged in successfully','success')
	return redirect(request.args.get('next') or url_for('admin'))