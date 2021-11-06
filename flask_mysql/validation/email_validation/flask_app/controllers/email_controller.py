from flask.helpers import flash
from flask.templating import render_template_string
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
    print(request.form)
    Email.add_new_email(request.form)
    flash(f"The email address you entered {request.form['email']} is a VALID email address! Thank you!")
    return redirect("/success")

@app.route("/success")
def display_emails():
    all_emails = Email.all_email()
    return render_template("success.html", all_emails = all_emails)

@app.route("/delete/<int:id>")
def remove_emails(id):

    Email.delete_email({"id": id})
    return redirect("/success")