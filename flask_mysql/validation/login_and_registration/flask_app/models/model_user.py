from flask.app import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

from flask import flash
import re

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

    # ADD CURD create update read delete
    @classmethod # select by EMAIL
    def select_one_email(self,data):
        query = "SELECT * FROM users WHERE email = %(email)s"

        results = connectToMySQL("registration_schema").query_db(query, data)

        if len(results) == 0:
            return False

        return User(results[0])

    @classmethod
    def select_one_id(self,data):
        query = "SELECT * FROM users WHERE id = %(id)s"

        results = connectToMySQL("registration_schema").query_db(query, data)

        if len(results) == 0:
            return False

        return User(results[0])


    @classmethod # create user
    def create_user(self, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUE (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"

        results = connectToMySQL("registration_schema").query_db(query, data)

        return results

    @staticmethod
    def in_valid(post_data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(post_data["first_name"]) < 2:
            flash("invalid first name")
            is_valid = False

        if len(post_data["last_name"]) < 2:
            flash("invalid last name")
            is_valid = False

        if not EMAIL_REGEX.match(post_data["email"]):
            flash("invalid email")
            is_valid = False
        else:
            user = User.select_one_email({"email": post_data["email"]})
            if user:
                flash("Try another email")
                is_valid = False

        if len(post_data["password"]) < 8:
            flash("invalid password")
            is_valid = False
        elif post_data["password"].isalpha():
            flash("at least 1 number required in password")
            is_valid = False
        elif not any(letter.isupper() for letter in post_data["password"]):
            flash("at least 1 uppercase required in password")
            is_valid = False

        if post_data["password"] != post_data["confirm_password"]:
            flash("password not match")
            is_valid = False

        return is_valid

    @staticmethod
    def log_in(post_data):
        user = User.select_one_email({"email": post_data["email"]})

        if not user:
            flash("no user in the record")
            return False

        if not bcrypt.check_password_hash(user.password, post_data["password"]):
            flash("wrong password")
            return False

        return True