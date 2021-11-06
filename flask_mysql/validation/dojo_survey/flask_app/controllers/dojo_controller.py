from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo_model import Dojo


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    if not Dojo.validate_info(request.form):
        return redirect ("/")

    # {% with messages = get_flashed_message() %}
    # {% if messages %}
    #     {% for message in messages %}
    #         <p>{{ message }}</p>
    #     {% endfor %}
    # {% endif %}
    # {% endwith %}

    Dojo.create_dojo(request.form)

    session["name"] = request.form["name"]           # assign request value to session
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect ("/result")

@app.route("/result")
def result():
    return render_template("result.html",
        name = session["name"],
        location = session["location"],
        language = session["language"],
        comment = session["comment"],
    )