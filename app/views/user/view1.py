# Author: ing.in
# -*- coding: utf-8 -*-

from . import user_app
from app import mail
from flask_mail import Message
from app.models import db,User
from loggings import logger

@user_app.route('/user', methods=['GET'])
def Userselect():
	print(list(map(lambda x:x.name,User.query.all())))
	return 'ok!!!'


@user_app.route('/adduser')
def AddUser():
	try:
		user = User(name='changhao1', password='ch134197', email='ing@foxmail.com')
		db.session.add(user)
		db.session.commit()
	except Exception as e:
		logger.error(e)
		db.session.rollback()
		return 'add failed'
	else:
		return 'add ok!!!'

@user_app.route("/index")
def index():

	return '<a href="/user/send_mail">发送邮件</a>'

@user_app.route("/send_mail")
def send_mail():
	message = Message('good luck',recipients=[
		'ing.in@foxmail.com',
		'c.evan@qq.com',
	     'changh@soyuan.com.cn'
	])
	message.html = '<h1>hahah</h1>'
	mail.send(message)
	return 'send mail succesfully'
