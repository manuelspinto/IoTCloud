from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

from IoTCloud import config

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from IoTCloud.dbm.deploy import deploy
deploy.CreateDefaultUsers()

from IoTCloud import views

