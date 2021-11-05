from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]             #assign self variable for all the return value
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    # CRUD Controller Read Update Delete

    # READ all db of Dojos
    @classmethod
    def display_all(cls):
        query = "SELECT * FROM dojos;" # query declartion

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query) # getting back the row of results
        dojos = []
        # print(results)
        for row in results:
            dojos.append(Dojo(row))
        return dojos

    # Update - add new dojo
    @classmethod
    def create_new_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at)VALUE (%(name)s,NOW(),NOW())"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data) # getting back the row of results
        return results

    # READ - read data from specific dojo
    @classmethod
    def display_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id  WHERE dojos.id = %(id)s;"
        print(query)
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        if len(results) == 0:
            return False


        return Dojo(results[0])