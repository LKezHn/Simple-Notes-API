from flask_restx import fields

def todo_model(api):

    todo_model = api.model("Todo", {
        "id": fields.String(description="Todo's ID", example="65f1a2b9c4d1e8f3a1b2c3d4"),
        "title": fields.String(required= True,description="Todo's title"),
        'description': fields.String(required= True,description="Todo's description"),
        'status': fields.String(required= True, default="Pending",description="Todo's status"),
    })

    return todo_model