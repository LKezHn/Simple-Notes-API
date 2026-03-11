from flask_pymongo import PyMongo

mongo = PyMongo()

def create_indexes():
    mongo.db.users.create_index("username", unique=True)
    mongo.db.users.create_index("email", unique=True)