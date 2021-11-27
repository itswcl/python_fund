from flask import render_template, request, redirect, jsonify

from flask_app import app
from flask_app.models.model_user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/users")
def get_all_users():
    return jsonify(users = User.get_all())


@app.route("/api/users/create", methods = ["POST"])
def create_user():
    print(request.json)
    User.create(request.json)
    return jsonify(message = "Add a user!")