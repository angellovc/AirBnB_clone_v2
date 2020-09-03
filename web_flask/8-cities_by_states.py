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


@app.route('/cities_by_states')
def cities_by_states():
    """ display all the states and the cities linked to  """
    return render_template(
        '8-cities_by_states.html',
        states=storage.all(State).values(),
        type_storage=getenv('HBNB_TYPE_STORAGE')
    )


@app.teardown_appcontext
def teardown_appcontext(error):
    """ remove the current SQLAlchemy Session After each request """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
