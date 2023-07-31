#!/usr/bin/python3
"""
Module for starting a Flask web application.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """
    Teardown method to close the current SQLAlchemy session.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """
    Route to display a list of all State objects present in DBStorage sorted by name.
    """
    states = sorted(list(storage.all(State).values()), key=lambda s: s.name)
    return render_template('states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
