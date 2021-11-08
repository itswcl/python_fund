from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.model_user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

# register the user
@app.route("/user/form/create", methods=["POST"])
def form_user_create():
    if not User.in_valid(request.form):
        return redirect("/")

    hash_password = bcrypt.generate_password_hash(request.form["password"])

    new_user = {
        **request.form,
        "password": hash_password
    }

    User.create_user(new_user)
    return redirect("/")

# display the user on dashboard
@app.route("/user/dashboard")
def dashboard():
    pass