#!/usr/bin/python3
""" Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


# Defines the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"
