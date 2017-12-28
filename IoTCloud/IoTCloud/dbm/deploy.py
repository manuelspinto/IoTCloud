from .rdb import db
from .models import User
import bcrypt

class Deploy():
	db.create_all()

	if User.query.filter_by(username='sysadmin').first() is None:
		en_pw = bcrypt.hashpw(b'sysadmin', bcrypt.gensalt())
		sysadmin = User('sysadmin',en_pw.decode('utf-8'),'sysadmin@iotcloud.com')
		en_pw = bcrypt.hashpw(b'masp', bcrypt.gensalt())
		admin = User('masp', en_pw.decode('utf-8'), 'manuelseixaspinto@gmail.com')
		db.session.add(sysadmin)
		db.session.add(admin)
		try:
			db.session.commit()
			print(":: Initial DBs deployed")
		except Exception as e:
			print(":: Exception occurred when trying to create default DBs:\n\tEx:{}".format(e))
		finally:
			db.session.close()
