from flask.helpers import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User

class Recipe:
    schema_file = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.under_30 = data["under_30"]
        self.instruction = data["instruction"]
        self.data_made_on = data["data_made_on"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = User.select_one_id({"id": data["user_id"]})

    # CRUD

    # create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description,under_30,instruction,data_made_on,created_at,updated_at,user_id)\
                VALUE (%(recipe_name)s, %(recipe_description)s, %(under_30)s, %(recipe_instruction)s, %(data_made_on)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.schema_file).query_db(query, data)
        # return the ID of user
        return results

    # Read many
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.schema_file).query_db(query)

        recipes = []
        for row in results:
            recipes.append(Recipe(row))
        return recipes

    # Read one
    @classmethod
    def select_one(cls, data):
        pass

    # update
    @classmethod
    def update(cls, data):
        pass

    # delete
    @classmethod
    def data(cls, data):
        pass

    @staticmethod
    def recipe_valida(post_data):
        is_valid = True

        if len(post_data["recipe_name"]) < 2:
            flash("Name is too short")
            is_valid = False

        if len(post_data["recipe_description"]) < 8:
            flash("Description is too short")
            is_valid = False

        if not "under_30" in post_data:
            flash("is it under 30 Minutes?")
            is_valid = False

        if len(post_data["recipe_instruction"]) < 8:
            flash("Instruction is too short")
            is_valid = False

        if len(post_data["data_made_on"]) < 4:
            flash("invalid date")
            is_valid = False

        return is_valid