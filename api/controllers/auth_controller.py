import bcrypt
from db import mongo

from pymongo.errors import DuplicateKeyError

from flask_jwt_extended import create_access_token

def register_user(username, email, password):
    
    # Hashing password for security
    encrypted_pass = bcrypt.hashpw( password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")

    try:
        user = mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": encrypted_pass
        })

        token = create_access_token(identity=str(user["_id"]))

        return token, None
    
    except DuplicateKeyError:
        return None, "username or email already exists"


def login_user(username, password):

    user = mongo.db.users.find_one({"username": username})

    if not user:
        return None, "Invalid credentials"

    if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        token = create_access_token(identity=str(user["_id"]))
        return token, None
    
    return None, "Invalid credentials"