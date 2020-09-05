#!/usr/bin/python3
""" starts a Flask web application """
from os import path, getenv
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

template_folder = path.abspath('/web_flask/static')
app = Flask(__name__, static_url_path=template_folder)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/hbnb_filters')
def hbnb_filters():
    states = storage.all(State).items()
    state_names = []
    for state, i in zip(states, range(0, 2)):
        state_names.append(state.name)

    return render_template(
        '10-hbnb_filters.html',
        states=storage.all(State).values(),
        state_names=state_names
    )


@app.teardown_appcontext
def teardown_appcontext(error):
    """ remove the current SQLAlchemy Session After each request """
    storage.close()

if __name__ == '__main__':
    app.run(host="172.28.128.4", port=5000, debug=True)
