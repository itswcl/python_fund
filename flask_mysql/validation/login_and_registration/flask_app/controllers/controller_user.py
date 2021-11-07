from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.model_user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/form")
def form_user():
    return render_template("index.html")

@app.route("/user/form/create", methods=["POST"])
def form_user_create():
    User.create_user(request.form)
    return redirect("/")