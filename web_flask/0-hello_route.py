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

if __name__ == "__main__":
    # Starts the Flask development server
    # Listen on all networks interfaces (0.0.0.0) and port 5000
    app.run(host="0.0.0.0", port=5000)
