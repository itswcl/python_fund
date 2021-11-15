from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_book import Book

class Author:
    db = "books"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # CRUD create read update delete
    # show all author
    @classmethod
    def read_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for row in results:
            authors.append(cls(row))
        return authors


    # show 1 author
    @classmethod
    def read_author(cls, data):
        query = "SELECT * FROM authors\
                LEFT JOIN fav_books ON author_id = authors.id\
                LEFT JOIN books ON book_id = books.id\
                WHERE authors.id = %(id)s"

        results = connectToMySQL(cls.db).query_db(query, data)

        if len(results) == 0:
            return False

        author = Author(results[0])
        author.books = []
        for row in results:
            book_data = {
                **row,
                "id": row["books.id"],
                "created_at": row["books.created_at"],
                "updated_at": row["books.updated_at"],
            }
            author.books.append(Book(book_data))

        return author


    # create
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at)\
                VALUE(%(name)s, NOW(), NOW())"
        connectToMySQL(cls.db).query_db(query, data)

    # delete author
    @classmethod
    def delete_author(cls, data):
        query = "DELETE FROM authors WHERE id = %(id)s"
        connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def is_valid(data):

        valid = True
        if len(data["name"]) < 2:
            valid = False

        return valid