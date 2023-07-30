#!/usr/bin/python3
"""
This is a simple Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display 'HBNB'"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
