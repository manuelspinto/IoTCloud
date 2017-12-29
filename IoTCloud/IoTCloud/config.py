
from IoTCloud import app



# config
app.config.update(
    DEBUG = True, # Comment this por production Server
	#SQLALCHEMY_DATABASE_URI = CS_Remote,
    SQLALCHEMY_DATABASE_URI = CS_Local,
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
)

app.secret_key = '46d18aa6-9eef-4dd1-acda-df2048eaf5e0'
cypher_key = 'astimegoesby'