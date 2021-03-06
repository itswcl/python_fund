from flask.app import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import model_recipe

from flask import flash
import re

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

schema_file = "recipes_schema"

class User:
    schema_file = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []

    # ADD CRUD create read update delete

    # create user
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUE (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"

        results = connectToMySQL(cls.schema_file).query_db(query, data)

        return results

    # read many by id
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.schema_file).query_db(query)

        users = []
        for row in results:
            users.append(User(row))
        return users

    # read one by email
    @classmethod # select by EMAIL
    def select_one_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL(cls.schema_file).query_db(query, data)

        if len(results) == 0:
            return False

        return User(results[0])


    # read one by id
    @classmethod
    def select_one_id(cls,data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.schema_file).query_db(query, data)

        if len(results) < 1:
            return False

        user = User(results[0])
        for row in results:

            row = {
                "id": row["recipes.id"],
                "user": user,
                "name": row["name"],
                "description": row["description"],
                "under_30": row["under_30"],
                "instruction": row["instruction"],
                "data_made_on": row["data_made_on"],
                "created_at": row["recipes.created_at"],
                "updated_at": row["recipes.updated_at"],
            }

            user.recipes.append(model_recipe.Recipe(row))

        return user


    # validation for register
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

    # log in validation
    @staticmethod
    def login_validation(post_data):
        user = User.select_one_email({"email": post_data["email"]})

        if not user:
            flash("no user in the record")
            return False

        if not bcrypt.check_password_hash(user.password, post_data["password"]):
            flash("wrong password")
            return False

        return True