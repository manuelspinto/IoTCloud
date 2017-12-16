"""
The flask application package.
"""

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

# config
app.config.update(
    DEBUG = True # Uncomment this por production Server
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

import IoTCloud.views
