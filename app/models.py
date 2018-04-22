# Author: ing.in
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(32),unique=True,index=True)
	user = db.relationship('User',backref='role')

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(32),unique=True,index=True)
	password = db.Column(db.String(32))
	email = db.Column(db.String(32),unique=True)
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))