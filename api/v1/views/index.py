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


@app_views.route("/stats", strict_slashes=Flase)
def stats_api():
    '''
    /stats endpoint will return JSON formatted stats on all data
    '''
    stats = {"amenities": Amenity, "cities": City, "places": Place, "reviews": Review, "states": State, "user": User }

    for s in stats:
        stats[s] = storage.count(stats[s])

    return jsonify(stats)
