# Author: ing.in
# -*- coding: utf-8 -*-

from flask import Flask
from flask_mail import Mail
from werkzeug.utils import import_string
# from app.views.user import user_app
# from app.views.admin import admin_app
from config import config_dict
from .models import  db

blueprints = [
	'app.views.user:user_app',
	'app.views.admin:admin_app',
]

mail = Mail()

def Create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config_dict[config_name])
	db.init_app(app)
	mail.init_app(app)
	for bp_name in blueprints:
		bp = import_string(bp_name)
		print(bp)
		app.register_blueprint(bp)
	# app.register_blueprint(user_app,url_prefix='/api/1')
	# app.register_blueprint(admin_app)

	return app,db
