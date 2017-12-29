from . import *


@app.route('/register' , methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	
	username = request.form['username']

	if User.query.filter_by(username=username).first() is not None:
		flash("User '{}' already exists".format(username), "danger")
		return redirect(url_for('register'))


	enc_pass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
	user = User(username, enc_pass.decode('utf-8') ,request.form['email'])
	db.session.add(user)
	try:
		db.session.commit()
	except Exception as e:
		flash("Could not register user. Exception '{}'".format(e),'danger')
		return redirect(url_for('register'))
	finally:
		db.session.close()
	flash('User successfully registered','success')
	return redirect(url_for('login'))
