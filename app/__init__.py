from flask import Flask

from app import app_config
# app = Flask(__name__)
app = Flask(__name__, instance_relative_config = True)
app.config.from_object(app_config["development"])

from . import question