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

# create display
@app.route("/recipes/form")
def form_recipe():
    return render_template("create_recipe.html")

# ----------------------- ACTION ROUTE -----------------------------------------------------
# create recipe
@app.route("/recipes/create", methods=["POST"])
def form_recipe_create():
    if not Recipe.recipe_valida(request.form):
        return redirect("/recipes/form")
    data = {
        **request.form,
        "user_id": session["uuid"]
    }

    Recipe.create(data)
    return redirect("/dashboard")