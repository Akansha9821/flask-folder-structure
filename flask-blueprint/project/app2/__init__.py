from flask import Blueprint, render_template

app2 = Blueprint("app2", __name__)

app2.route('/')
def home():
    return "Hii this is app2"