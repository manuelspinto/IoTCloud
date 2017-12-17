from IoTCloud.dbm.rdb import db
from IoTCloud.dbm.models import User

class Deploy():
    def __init__(self):
        sysadmin = User('sysadmin','sysadmin','sysadmin@iotcloud.com')
        admin = User('masp', 'masp', 'manuelseixaspinto@gmail.com')
        db.session.add(sysadmin)
        db.session.add(admin)
        db.session.commit()
        print("DEPLOYED")
