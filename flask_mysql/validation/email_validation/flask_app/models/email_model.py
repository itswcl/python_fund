from flask_app.config.mysqlconnection import connectToMySQL

class Email:
    def __init__(self, data):
        self.id = data["id"]                    # from ERD
        self.email = data["email"]              # from ERD order
        self.created_at = data["created_at"]    # from ERD order
        self.updated_at = data["updated_at"]    # from ERD order

    @classmethod
    def add_new_email(cls, data):
        query = "INSERE INTO emails (email, created_at, update_at) VALUE (%(email)s, NOW(), NOW())"

        results = connectToMySQL("email_schema").query_db(query ,data)

        return results
