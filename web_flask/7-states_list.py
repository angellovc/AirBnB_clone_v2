#!/usr/bin/python3
""" starts a Flask web application """
from os import path
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

template_folder = path.abspath('./web_flask/templates/')
app = Flask(__name__, template_folder=template_folder)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/states_list')
def states_list():
    """ display State objects present in DBStorage  """
    return render_template(
        '7-states_list.html',
        states=storage.all(State).values())


@app.teardown_appcontext
def teardown_appcontext(error):
    """ remove the current SQLAlchemy Session After each request """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
