from flask_app import app # import our initialing app
from flask import render_template, redirect, request # import render/redirect/request for route purpose

from flask_app.models.email_model import Email # import the Class

@app.route("/") # initial the index page
def index():
    return render_template("index.html")

@app.route("/email/form") # route for form
def form():
    return render_template("index.html")

@app.route("/email/add", methods=["POST"]) # route for POST request
def add():
    if not Email.validate(request.form):
        return redirect("/")

    Email.add_new_email(request.form)
    return redirect("/")
