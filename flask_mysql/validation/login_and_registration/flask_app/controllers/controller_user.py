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

    User.create_user(request.form)
    return redirect("/")