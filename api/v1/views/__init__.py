#!/usr/bin/python3
'''
    Views BluePrint
'''
from api.v1.views.index import *
from flask import Blueprint

'''a variable app_views which is an instance of Blueprint '''
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
