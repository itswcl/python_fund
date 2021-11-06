from flask.templating import render_template_string
from flask_app import app # import our initialing app
from flask import render_template, redirect, request # import render/redirect/request for route purpose

from flask_app.models.email_model import Email # import the Class

@app.route("/") # initial the index page
def index():
    return render_template("index.html")