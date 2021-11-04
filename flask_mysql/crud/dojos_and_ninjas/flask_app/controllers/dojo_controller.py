from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    # Dojo.display_all()
    return render_template("index.html", dojos = Dojo.display_all())