from crypt import methods
from flask_app.modular import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy




app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://root:@server/blog?driver=SQL+Server"
db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))  
    phone = db.Column(db.String(200))
    message = db.Column(db.String(10))




@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        r_name = request.form['name']
        r_email = request.form['email']
        r_phone = request.form['phone']
        r_message = request.form['message']

        query = Contacts(name=r_name, email=r_email, phone=r_phone, message=r_message)
        db.session.add(query)
        db.session.commit()

    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')