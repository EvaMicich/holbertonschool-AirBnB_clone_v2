#!/usr/bin/python3
"""starts flask web app with variable route"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_cool(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
