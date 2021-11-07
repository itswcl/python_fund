from flask_app.config.mysqlconnection import connectToMySQL
import re

class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

    # ADD CURD create update read delete
    @classmethod
    def create_user(self, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUE (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"

        results = connectToMySQL("registration_schema").query_db(query, data)

        return results

    @staticmethod
    def in_valid(post_data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



        return is_valid