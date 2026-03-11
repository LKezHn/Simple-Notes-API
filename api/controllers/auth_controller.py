from db import mongo
from pymongo.errors import DuplicateKeyError

def register_user(username, email, password):
    
    try:
        mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": password
        })

        return "User registered", None
    except DuplicateKeyError:
        return None, "username or email already exists"
