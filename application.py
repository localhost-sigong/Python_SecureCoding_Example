from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' #TODO
db = SQLAlchemy(app)

login_manager

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text, unique=True)

    def __init__(username, password):
        self.username = username
        self.password = password

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signUp", methods=["POST"])
def register():
    if request.form["username"] = "" or request.form["password"] = "":
        return render_template("sign_up.html")
    user = User(request.form["username"], request.form["password"])
    db.session.add(user)
    db.session.commit()
    return render_template("success.html")

@app.route("/login", methods=["POST", "GET"]):
def login():
    if request.method == "GET":
        return render_template("index.html")
        # index.html is the login/homepage
    elif request.method == "POST":
        if request.form["username"] and request.form["password"]:
            user = User.query.filter_by(username=request.form["username"]).first()
            if user is not none:
                return render_template("loged_on.html")