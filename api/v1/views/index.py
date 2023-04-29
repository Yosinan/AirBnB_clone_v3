#!/usr/bin/python3
'''
    Views BLuePrint
'''
from flask import Flask
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def statusApi():
    '''
    returns a JSON: "status": "OK"
    '''
    return jsonify(status="OK")
