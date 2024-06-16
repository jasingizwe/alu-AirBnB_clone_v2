#!/usr/bin/python3
""" Write a script that starts a Flask web application,
Web application is listening on 0.0.0.0, port 5000 """

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_route():
    """cities_route"""
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
