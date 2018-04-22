# Author: ing.in
# -*- coding: utf-8 -*-

from flask import Blueprint
user_app = Blueprint('user_app',__name__,url_prefix='/user')

from . import view2,view1
