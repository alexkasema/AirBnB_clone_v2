#!/usr/bin/python3

""" Hello Flask! simple flask app """

from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
