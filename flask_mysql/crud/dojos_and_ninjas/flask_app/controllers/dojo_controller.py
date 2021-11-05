from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    # Dojo.display_all()
    return render_template("index.html", dojos = Dojo.display_all())

@app.route("/dojos/form")
def form_new_dojo():
    return render_template("index.html") # refresh page to show form data

@app.route("/dojos/formcreate", methods=["POST"])
def create_new_dojo():
    Dojo.create_new_dojo(request.form) # pass the value from form to Dojo
    return redirect("/") # redirect to front page after POST sent

@app.route("/dojos/<int:dojo_id>")
def select_one_dojo(dojo_id):
    return render_template("dojo.html", dojos = Dojo.display_one({"id": dojo_id}))
