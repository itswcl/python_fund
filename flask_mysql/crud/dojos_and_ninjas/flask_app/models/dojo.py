from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.name = data["name"]             #assign self variable for all the return value
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # CRUD ControllerReadUpdateDelete

    # READ all db of Dojos
    @classmethod
    def display_all(cls):
        query = "SELECT * FROM dojos;" # query declartion

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query) # getting back the row of results
        dojos = []
        print(results)
        for row in results:
            dojos.append(Dojo(row))
        return dojos

