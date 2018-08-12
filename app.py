from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/DHT.db'
SQLALCHEMY_BINDS = {
    #'picam':        'sqlite:///db/picam.db',
    #'comments':     'sqlite:///Comments.db'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes import *



if __name__ == '__main__':
    try:
        app.run(debug=True, port=80, host='0.0.0.0')
    except Exception as e:
        print(e)
