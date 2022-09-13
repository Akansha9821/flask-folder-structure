from flask import Flask
from project.app1 import app1
from project.app2 import app2
from project.main import main


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(app1)
    app.register_blueprint(app2)

    return app