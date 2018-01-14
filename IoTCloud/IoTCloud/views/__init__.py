from flask import render_template, request, flash, url_for, redirect, render_template, abort ,g
from flask_login import login_required, login_user, logout_user , login_manager, current_user
from flask_wtf import FlaskForm
import bcrypt
from datetime import datetime
from .. import app, login_manager
from ..dbm.models import User

from ..dbm.rdb import * 
from ..dbm.deploy import *

from .general import *
from .index import *
from .login import *
from .logout import *
from .register import *
from .admin import *

