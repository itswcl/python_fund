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

# display the recipe
@app.route("/recipes/<int:id>")
def detail_recipe(id):
    return render_template(
        "detail_recipe.html",
        recipe = Recipe.select_one({"id": id})
    )

# display the recipe
@app.route("/recipes/<int:id>/edit")
def edit_recipe(id):
    return render_template(
        "edit_recipe.html",
        recipe = Recipe.select_one({"id": id})
    )

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

# update recipe
@app.route("/recipes/<int:id>/update", methods=["POST"])
def form_recipe_update(id):
    if not Recipe.recipe_valida(request.form):
        return redirect(f"/recipes/{id}/edit")

    data = {
        **request.form,
        "id": id
    }

    Recipe.update(data)
    return redirect("/dashboard")

# delete recipe
@app.route("/recipes/<int:id>/delete")
def recipe_delete(id):
    Recipe.delete({"id": id})
    return redirect("/dashboard")