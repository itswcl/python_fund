from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "ajax_users"
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = '''
                INSERT INTO users (username, email, created_at, updated_at)
                VALUE (%(username)s, %(email)s, NOW(), NOW())
                '''
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_one_by_name(cls, data):
        query = '''
                SELECT * FROM users WHERE username = %(username)s
                '''
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            return cls(results[0])

    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM users
                '''
        results = connectToMySQL(cls.db).query_db(query)

        users = []
        for row in results:
            users.append(row)
        return users
