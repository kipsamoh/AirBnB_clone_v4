#!/usr/bin/python3
""" _Starts a Flash Web _Application Python is _Cool"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ _Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ _Prints a Mess_age when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ _Prints a Message when /c is called """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """ Prints a Messa_ge when /python is called """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    """ Prints a Mes_sage when number is cal-led only if n is an int"""
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    """ Main F_unction """
    app.run(host='0.0.0.0', port=5000)
