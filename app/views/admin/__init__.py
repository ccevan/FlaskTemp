# Author: ing.in
# -*- coding: utf-8 -*-

from flask import Blueprint

admin_app = Blueprint('role_app',__name__)

from . import view2,view1