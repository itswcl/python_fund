from flask.globals import request
from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        # dictionary to hold data
        # field the data from ERD and attribute for our class
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# READ ALL
    @classmethod
    def get_all(cls): #class method for cls #function name for query
        # first query
        query = "SELECT * FROM users;"

        # query the db and save the result from query
        results = connectToMySQL("users_schema").query_db(query) # note str name from the sql
        # work the data
        users = []
        # row is the dictionary
        for row in results:
            users.append(User(row))

        # return
        return users


# CREATE
    @classmethod
    def create(cls, data):
        # data as dictionary to put value into str
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUE (%(first_name)s, %(last_name)s, %(email)s, NOW(),NOW())"
        results = connectToMySQL("users_schema").query_db(query, data) # note str name from the sql

        return results

# READ ONE
    @classmethod
    def get_one(cls, data):
        # data dictionary and only holds 1 value of ID ex {'id' = 1}
        # and the 1 is different each user
        query = "SELECT * FROM users WHERE id = %(id)s"
        # result still the dictionary
        results = connectToMySQL("user_schema").query_db(query, data)

        # double check if the result has only 1 value of dictionary
        # to avoid break from python
        if len(results) == 0:
            return False

        # get the only dictionary and run User Class
        return User(results[0])


# UPDATE
    @classmethod
    def update_value(cls, data):
        # query
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"
        # get the data in order for us to update from query
        results = connectToMySQL("user_schema").query_db(query, data)
        # update
        return results


# DELETE
    @classmethod
    def remove_user(cls, data):
        # query
        query = "DELETE FROM users WHERE id = %(id)s"
        # don't need to use the data so we run the query
        connectToMySQL("user_schema").query_db(query, data)
