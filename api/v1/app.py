#!/usr/bin/pyhton3
'''
    start a Flask Web-App
'''

from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def db_teardown(exception):
    ''' close storage on teardown '''
    storage.close()


if __name__ == '__main__':
    app.run(getenv('HBNB_API_HOST') or '0.0.0.0', getenv('HBNB_API_PORT') or 5000)
