from flask import Flask, render_template

app = Flask(__name__)


from flask_app.modular import routes