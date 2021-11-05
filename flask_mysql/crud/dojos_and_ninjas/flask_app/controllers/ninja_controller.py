from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas/form")
def form_new_ninja():
    return render_template("new_ninja.html", all_dojos = Dojo.display_all())

@app.route("/ninjas/formcreate", methods = ["POST"])
def create_ninja():
    # print(request.form)
    Ninja.create_new_ninja(request.form)
    return redirect ("/")