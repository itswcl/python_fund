from flask.app import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
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

        if len(post_data["first_name"]) < 2:
            flash("invalid first name")
            is_valid = False

        if len(post_data["last_name"]) < 2:
            flash("invalid last name")
            is_valid = False

        if not EMAIL_REGEX.match(post_data["email"]):
            flash("invalid email")
            is_valid = False

        if len(post_data["password"]) < 8:
            flash("invalid password")
            is_valid = False

        if post_data["password"] != post_data["confirm_password"]:
            flash("password not match")
            is_valid = False

        return is_valid