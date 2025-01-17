#!/usr/bin/python3
'''
    start a Flask Web-App
'''

from flask import Flask, jsonify, make_response
from os import getenv
from api.v1.views import app_views
from models import storage
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def db_teardown(exception):
    ''' close storage on teardown '''
    storage.close()


@app.errorhandler(404)
def pageNotFound(error):
    '''
    404 response in JSON format
    '''
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    app.run(host or '0.0.0.0',
            port or 5000,
            threaded=True)
