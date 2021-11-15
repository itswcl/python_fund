from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Book:
    db = "books"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    #CRUD
    # READ ALL
    @classmethod
    def read_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.db).query_db(query)

        if len(results) == 0:
            return False
        books = []
        for row in results:
            books.append(Book(row))
        return books

    # READ ALL BY author id
    @classmethod
    def read_books_author(cls, data):
        query = "SELECT * FROM books\
                LEFT JOIN fav_books ON books.id = book_id\
                LEFT JOIN authors ON author.id = author_id\
                WHERE authors.id = %(id)s"

        results = connectToMySQL(cls.db).query_db(query, data)

        if not results:
            return False

        books = []
        for row in results:
            data = {
                "id" : row["books.id"],
                "title" : row["books.title"],
                "num_of_pages" : row["books.num_of_pages"],
                "created_at" : row["books.created_at"],
                "updated_at" : row["books.updated_at"]
            }
            books.append(Book(data))
        return books


    # create
    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages)\
                VALUE (%(title)s, %(num_of_pages)s)"

        connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def is_valid(data):

        valid = True
        if len(data["title"]) < 2:
            valid = False

        return valid