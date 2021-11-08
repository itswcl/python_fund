from flask import render_template, request, redirect,session

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

    new_user = {
        **request.form,
        # bcrypt the pass word for the user
        "password": bcrypt.generate_password_hash(request.form["password"])
    }

    # save to session while creating the new user
    session["uuid"] = User.create_user(new_user)

    return redirect("/dashboard")

# display the user on dashboard
@app.route("/dashboard")
def dashboard():
    if not "uuid" in session:
        return redirect("/")

    user = User.select_one_id({"id": session["uuid"]})
    return render_template("dashboard.html", user = user)

# log out = clean out session
@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")

# log in route
@app.route("/login", methods=["POST"])
def form_user_login():
    if not User.log_in(request.form):
        return redirect("/")

    user = User.select_one_email({"email": request.form["email"]})
    print(user)
    session["uuid"] = user.id

    return redirect("/dashboard")
