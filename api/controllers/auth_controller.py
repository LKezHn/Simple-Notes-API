from db import mongo
from pymongo.errors import DuplicateKeyError

def register_user(username, email, password):
    
    mongo.db.users.insert_one({
        "username": username,
        "email": email,
        "password": password
    })