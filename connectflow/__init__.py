import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)








#########################
#### BLUEPRINT SETUP ####
#########################
from connectflow.core.views import core
app.register_blueprint(core)
