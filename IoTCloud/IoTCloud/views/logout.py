from . import *

@app.route("/logout")
@login_required
def logout():
	logout_user()
	flash('Logged out successfully','success')
	return redirect(url_for('home'))