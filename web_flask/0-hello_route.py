#!/usr/bin/python3
"""Inicia la aplicación web Flask

Aplicación listen a 0.0.0.0, puerto 5000.
Routes:
    /: Retorna 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Retorna 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")