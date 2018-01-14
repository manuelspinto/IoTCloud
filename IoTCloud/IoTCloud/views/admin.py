from . import *

@app.route("/admin", methods=['GET','POST'])
@login_required
def admin():
	flash('Wecome to the admin page','warning')

	if request.method == 'GET':
		return render_template('admin.html',
								title='Admin Page',
								message='Get started!')
	flash('Creating databases please wait...','warning')
	retmsg = deploy.CreateInstanceDBs(current_user.username)

	return render_template('admin.html',
								title='Admin Page',
								message='Get started!')
	

