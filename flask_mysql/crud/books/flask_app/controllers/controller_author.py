from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.model_author import Author
from flask_app.models.model_book import Book


############### display route ##################
@app.route("/")
def index():
    authors = Author.read_authors()

    return render_template("index.html", authors = authors)

@app.route("/authors/<int:id>")
def show_author(id):

    author = Author.read_author({"id": id})
    books = Book.read_books()

    return render_template(
        "author.html",
        author = author,
        books = books
    )


############### action route ##################
@app.route("/authors/form_create", methods=["POST"])
def create_authors():
    if not Author.is_valid(request.form):
        return redirect("/")

    Author.create_author(request.form)
    return redirect("/")

@app.route("/authors/<int:id>/favorite", methods=["GET"])
def create_author_favorite(id):
    print(request.form)

    # Author.create_author(request.form)
    return redirect(f"/authors/{id}")