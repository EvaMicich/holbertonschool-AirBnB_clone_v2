#!/usr/bin/python3
"""Starts up Flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
