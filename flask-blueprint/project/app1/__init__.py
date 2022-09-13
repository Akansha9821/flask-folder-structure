from flask import Blueprint, render_template

app1 = Blueprint("app1", __name__)

app1.route('/')
def home():
    return "Hii this is app1"