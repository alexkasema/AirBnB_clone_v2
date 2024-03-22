#!/usr/bin/python3

""" Hello Flask! simple flask app """

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ route that displays some text """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ route that displays HBNB """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def text(text=None):
    "Gets arguments from the url"
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def text_python(text='is_cool'):
    """ Gets arguments from the url and displays it """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n=None):
    """ display “n is a number” only if n is an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_temp(n=None):
    """ renders a template and passes to it the number from the url """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_odd(n=None):
    """ renders a template and passes to it the number from the url """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
