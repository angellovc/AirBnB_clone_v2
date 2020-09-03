#!/usr/bin/python3
""" starts a Flask web application """
from os import path, getenv
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/states', strict_slashes=False)
def states():
    """ display all the states """
    return render_template(
        '9-states.html',
        states=storage.all(State).values(),
        id=None
    )


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """ display a state name and the cities linked to  """
    state_id = "State."+id
    state = storage.all(State).get(state_id)
    if (state is None):
        state_name = None
        cities = None
        id = None
    else:
        state_name = state.name
        cities = state.cities
    return render_template(
        '9-states.html',
        state=state_name,
        cities=cities,
        id=id
    )


@app.teardown_appcontext
def teardown_appcontext(error):
    """ remove the current SQLAlchemy Session After each request """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
