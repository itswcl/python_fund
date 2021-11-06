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

    # READ ALL
    @classmethod
    def all_email(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL("email_schema").query_db(query)

        email_list = []
        for row in results:
            email_list.append(Email(row))

        return email_list

    # READ ONE
    @classmethod
    def one_email(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s"

        results = connectToMySQL("email_schema").query_db(query, data)
        if len(results) == 0:
            return False

        return Email(results[0])

    # UPDATE
    @classmethod
    def add_new_email(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUE (%(email)s, NOW(), NOW())"

        results = connectToMySQL("email_schema").query_db(query ,data)
        return results

    # Delete
    @classmethod
    def delete_email(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        connectToMySQL("email_schema").query_db(query, data)


    @staticmethod # static method for validation of input value
    def validate(post_data):
        is_valid = True
        # condition for input email also need the message
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data["email"]): # match input email if has validate data
            # not "True" return false meaning has validated
            # not "False" return true meaning has not validated
            flash("email input is invalid")
            is_valid = False
        else:
            if Email.one_email({"email": post_data["email"]}):
                flash("email has been used")
                is_valid = False

        return is_valid # result data if validated or not