from .rdb import *
from .models import User
import bcrypt

class deploy():
	def CreateDefaultUsers():
		print(":: CreateDefaultUsers")
		print(":: Creating Default DBs")
		db.create_all()

		print(":: Creating Defautl Users")
		if User.query.filter_by(username='sysadmin').first() is None:
			en_pw = bcrypt.hashpw(b'sysadmin', bcrypt.gensalt())
			sysadmin = User('sysadmin',en_pw.decode('utf-8'),'sysadmin@iotcloud.com')
			en_pw = bcrypt.hashpw(b'masp', bcrypt.gensalt())
			admin = User('masp', en_pw.decode('utf-8'), 'manuelseixaspinto@gmail.com')
			db.session.add(sysadmin)
			db.session.add(admin)
			try:
				db.session.commit()
				print(":: Defautl Users created")
			except Exception as e:
				print(":: Exception occurred when trying to create default users:\n\tEx:{}".format(e))
			finally:
				db.session.close()
		else:
			print(':: Default users already created')
	def CreateInstanceDBs(username):
		def CreateDB(dbname):	
			print(":: Creating Database '{}'".format(dbname))
			engine = create_engine("postgres://sa:sysadmin@localhost:5432/{}".format(dbname))
			retmsg = ''
			if not database_exists(engine.url):
				create_database(engine.url)
				retmsg = ["Database '{}' created successfully".format(dbname),"success"]
			else:
				retmsg = ['Error: Database already exists' , 'danger']
			return retmsg

		dbname = "{}_IoTCloudMain".format(username) 
		retmsg = CreateDB(dbname)
		flash(retmsg[0] , retmsg[1])
		dbname = "{}_IoTCloudReporting".format(username) 
		retmsg += CreateDB(dbname)
		flash(retmsg[0] , retmsg[1])
		
		