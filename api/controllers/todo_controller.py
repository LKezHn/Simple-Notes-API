from db import mongo 

def get_todos():
    todos = mongo.db.todos.find()
    result = []

    for todo in todos:
        result.append({
            "id": str(todo["_id"]),
            "title": todo.title,
            "description": todo.description,
            "status": todo.status
        })

    return result
