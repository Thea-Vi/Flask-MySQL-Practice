import dataclasses
from mysqlconnection import connectToMySQL

# 1
class User:
    def __init__(self, data):
        # place the fields/columns
        
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # query first before instantiate
    # goal is to get all users before creating an object
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # query_db() function to query the database
        results = connectToMySQL("users_schema").query_db(query)
    
        # convert dictionary (results) to objects
        users = []
        for row in results:
            # loops through the dictionary
            # each dictionary, instantiate a user
            users.append(cls(row)) 
            
        return users
      
        
        # DONT FORGET TO import user from User to server.py
        #  how to render the list of users to template??
        #  -- go to server.py and add ----
        # @app.route('/')
            # def index():
            #     all_users = User.get_all()
            #     return render_template('index.html', all_users = all_users)

        
        
       #6 make a query - ADD USER
    @classmethod
    def create(cls, data):
    #    DATA IS A DICTIONARY - HOW TO ACCESS?
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        # pass data
        results = connectToMySQL("users_schema").query_db(query, data)
        
        return results