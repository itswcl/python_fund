from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.model_book import Book

############### display route ##################
@app.route("/books")
def indexBook():
    books = Book.read_books()
    return render_template("books.html", books = books)

############### action route ##################
@app.route("/books/form_create", methods=["POST"])
def create_books():
    if not Book.is_valid(request.form):
        return redirect("/")

    Book.create_book(request.form)
    return redirect("/books")
