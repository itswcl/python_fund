from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]

    # controller methods for Create / Read / Update / Delete
    @classmethod # classmethod pass in cls / cls, data
    def view_all(cls):
        query = "SELECT * FROM dojos"

        results = connectToMySQL("dojo_survey_schema").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(Dojo(dojo))
        return dojos

    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUE (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW())"

        results = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return results