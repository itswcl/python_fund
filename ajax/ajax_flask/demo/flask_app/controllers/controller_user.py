from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.model_user import User

@app.route("/")
def index():
    return render_template("index.html")