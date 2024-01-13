#!/usr/bin/python3
"""HolbertonBnB main Flask application.

The application listens on host IP 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Retorna 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')