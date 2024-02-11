#!/usr/bin/python3
""" Starts a Flash Web App_lication """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Mess_age when / is called """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Main Func_tion """
    app.run(host='0.0.0.0', port=5000)
