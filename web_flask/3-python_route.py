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

@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Display 'C ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is_cool'):
    """Display 'Python ' followed by the value of the text variable (default: 'is_cool')"""
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
