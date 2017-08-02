from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db' #TODO
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text, unique=True)

    def __init__(username, password):
        self.username = username
        self.password = password

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_up", methods=["POST"])
def register():
    if request.form["username"] == "" or request.form["password"] == "":
        return render_template("index.html")
    user = User(request.form["username"], request.form["password"])
    db.session.add(user)
    db.session.commit()
    return render_template("success.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("index.html")
        # index.html is the login/homepage
    elif request.method == "POST":
        if request.form["username"] and request.form["password"]:
            user = User.query.filter_by(username=request.form["username"]).first()
            if user is not none:
                return render_template("success.html")
