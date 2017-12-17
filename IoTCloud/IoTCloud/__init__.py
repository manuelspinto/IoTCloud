from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

# config
app.config.update(
    DEBUG = True, # Comment this por production Server
    SQLALCHEMY_DATABASE_URI = 'postgres://tmlavqsg:wGTiOq8ydTXod6hoiYySWFC82ZAxnLhI@horton.elephantsql.com:5432/tmlavqsg',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from IoTCloud import views

