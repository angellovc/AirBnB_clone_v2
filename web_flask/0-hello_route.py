#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask


app = Flask(__name__)
if __name__ == '__main__':
    app.run(host="0,0,0,0", port=5000)


@app.route('/', strict_slashe=False)
def display_hello():
    """ display "Hello HBNB!" when '/' route
    is requested
    """
    return "Hello HBNB!"
