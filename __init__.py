from flask import Flask

app = Flask(__name__)
app.config.from_object('matsuri.config')

import flask_zemi.views