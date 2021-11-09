from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.under_30 = data["under_30"]
        self.instruction = data["instruction"]
        self.data_made_on = data["data_made_on"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = user.User.select_one_id({"id": data["user_id"]})

    # CRUD

    # create
    @classmethod
    def create(cls, data):
        pass

    # Read many
    def select_all(cls, data):
        pass

    # Read one
    def select_one(cls, data):
        pass

    # update
    def update(cls, data):
        pass

    # delete
    def data(cls, data):
        pass

    @staticmethod
    def recipe_valida():
        pass