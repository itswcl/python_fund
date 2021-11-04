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

    @classmethod
    def create(cls, data):
        # data as dictionary to put value into str
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUE (%(first_name)s, %(last_name)s, %(email)s, NOW(),NOW())"
        results = connectToMySQL("users_schema").query_db(query, data) # note str name from the sql

        return results;