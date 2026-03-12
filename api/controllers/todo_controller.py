from bson import ObjectId
from bson.json_util import dumps

from pymongo import ReturnDocument

from db import mongo 

def get_todos(user_id):
    todos = mongo.db.todos.find({"user_id": user_id})
    result = []

    for todo in todos:
        result.append({
            "id": str(todo["_id"]),
            "title": todo["title"],
            "description": todo["description"],
            "status": todo["status"]
        })

    return result

def add_todo(title, description, status, user_id):
    
    todo = mongo.db.todos.insert_one({
        "user_id": user_id,
        "title": title,
        "description": description,
        "status": status
    })
    
    return "%s"%todo.inserted_id

def get_todo(todo_id, user_id):
    todo = mongo.db.todos.find_one({"_id": ObjectId(todo_id), "user_id": user_id})
    if not todo:
        return None, "Not found"
    
    todo["_id"] = str(todo["_id"])

    return todo, None

def update_todo(todo_id, user_id, title, description, status):
    todo = mongo.db.todos.find_one_and_update({"_id": ObjectId(todo_id), "user_id": user_id}, { "$set": { "title": title, "description": description, "status": status}}, return_document=ReturnDocument.AFTER)

    if not todo:
         return None, "Not found"
    
    todo["_id"] = str(todo["_id"])

    return todo, None

def delete_todo(todo_id, user_id):
    todo = mongo.db.todos.find_one_and_delete({"_id": ObjectId(todo_id), "user_id": user_id})

    if not todo:
        return None, "Not found"
    
    todo["_id"] = str(todo["_id"])

    return "Todo was deleted", None