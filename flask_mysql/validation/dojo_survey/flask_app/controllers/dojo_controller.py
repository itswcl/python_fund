from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo_model


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    session["name"] = request.form["name"]           # assign request value to session
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    # session["season"] = request.form["season"]
    # session["device"] = request.form["device"]

    return redirect ("/result")

@app.route("/result")
def result():
    name = session["name"]
    location = session["location"]
    language = session["language"]
    comment = session["comment"]
    # season = session["season"]
    # device = session["device"]

    return render_template("result.html",
        name = name,
        location = location,
        language = language,
        comment = comment,
        # season = season,
        # device = device
        )