#!/usr/bin/python3
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
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    app.run(host=host if host is not None else '0.0.0.0',
            port=port if port is not None else 5000,
            threaded=True,
    )
