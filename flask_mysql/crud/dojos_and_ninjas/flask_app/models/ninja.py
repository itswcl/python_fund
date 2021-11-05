from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_new_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at)VALUE (%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW())"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data) # getting back the row of results
        return results