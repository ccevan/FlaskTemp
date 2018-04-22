# Author: ing.in
# -*- coding: utf-8 -*-
import os


class Config:
	DEBUG=True

class SonConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql://root:changhao@127.0.0.1/flask_user'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = "smtp.163.com"
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_DEFAULT_SENDER = 'flask<15890396381@163.com>'
	# MAIL_PASSWORD = os.environ.get('mail_password')

config_dict = {
	'SonConfig':SonConfig
}