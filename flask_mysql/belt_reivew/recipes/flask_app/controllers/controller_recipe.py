from flask import render_template, request, redirect,session

from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe


# ----------------------- DISPLAY ROUTE -----------------------------------------------------
# display the user on dashboard
@app.route("/dashboard")
def dashboard():
    if not "uuid" in session:
        return redirect("/")

    user = User.select_one_id({"id": session["uuid"]})
    return render_template(
        "dashboard.html",
        logged_user = user,
        recipes = Recipe.select_all()
        )

# ----------------------- ACTION ROUTE -----------------------------------------------------
# create recipe
@app.route("/recipes/create", methods=["POST"])
def form_recipe_create():
    pass