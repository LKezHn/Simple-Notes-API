import bcrypt
from db import mongo
from pymongo.errors import DuplicateKeyError

def register_user(username, email, password):
    
    # Hashing password for security
    encrypted_pass = bcrypt.hashpw( password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")

    try:
        mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": encrypted_pass
        })

        return "User registered", None
    
    except DuplicateKeyError:
        return None, "username or email already exists"


def login_user(username, password):

    user = mongo.db.users.find_one({"username": username})

    if not user:
        return None, "Invalid credentials"

    if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        return "User logged", None
    
    return None, "Invalid credentials"