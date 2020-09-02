#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ display Hello HBNB! when / route is requested """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display HBNB when /hbnb route is requested """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ C followed by the value of the text """
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ python followed by the value of the text """
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display n only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """ display n only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
