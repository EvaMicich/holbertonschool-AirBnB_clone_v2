#!/usr/bin/python3
"""Script that start Flask web app"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ displays all cities"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
