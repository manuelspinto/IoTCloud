from . import *

@app.route("/admin")
@login_required
def admin():
	flash('Wecome to the admin page','warning')
	return render_template('admin.html',
        title='Admin Page')