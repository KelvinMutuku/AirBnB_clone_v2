#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello():
    """Prints hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def desplay_hbnb():
    """Print hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_cText(text):
    """Print C with passed variable"""
    text = text.replace("_", " ")
    return "C %s" % (text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_pythonText(text='is cool'):
    """ Function called with /python/<text> route """
    if text != 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % (text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_if_int(n):
    return '%d is a number' % (n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_render_num(n):
    """Render template if number is an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_render_even_odd(n):
    """Render template if number is an integer
    identify if number is odd or even"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
