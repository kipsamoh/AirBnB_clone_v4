#!/usr/bin/python3
""" Starts a Flash _Web Application """
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the _current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=""):
    """ displays a HTML page with a list of cities by states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    _found = 0
    state = ""
    cities = []

    for i in states:
        if id == i.id:
            state = i
            _found = 1
            break
    if _found:
        states = sorted(state.cities, key=lambda k: k.name)
        state = state.name

    if id and not _found:
        _found = 2

    return render_template('9-states.html',
                           state=state,
                           array=states,
                           _found=_found)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
