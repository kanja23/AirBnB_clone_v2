
#!/usr/bin/python3
"""
Module for starting a Flask web application.
"""

from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """
    Teardown method to close the current SQLAlchemy session.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """
    Route to display a list of all State objects present in DBStorage sorted by name,
    along with the list of City objects linked to each State sorted by name.
    """
    states = sorted(list(storage.all(State).values()), key=lambda s: s.name)
    return render_template('cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
