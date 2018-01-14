
from IoTCloud import app


# config
app.config.update(
    DEBUG = True, # Comment this por production Server
	#SQLALCHEMY_DATABASE_URI = CS_Remote,
    SQLALCHEMY_DATABASE_URI = CS_Local,
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
)
