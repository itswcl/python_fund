from flask.app import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Email:
    def __init__(self, data):
        self.id = data["id"]                    # from ERD
        self.email = data["email"]              # from ERD order
        self.created_at = data["created_at"]    # from ERD order
        self.updated_at = data["updated_at"]    # from ERD order



    # UPDATE
    @classmethod
    def add_new_email(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUE (%(email)s, NOW(), NOW())"

        results = connectToMySQL("email_schema").query_db(query ,data)

        return results

    @staticmethod # static method for validation of input value
    def validate(post_data):
        is_valid = True
        # condition for input email also need the message
        if len(post_data["email"]) < 3:
            flash("length is invalid")
            is_valid = False
        else:
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(post_data["email"]): # match input email if has validate data
                # not "True" return false meaning has validated
                # not "False" return true meaning has not validated
                flash("email input is invalid")
                is_valid = False

        return is_valid # result data if validated or not