from flask_restx import fields

def todo_model(api):

    todo_model = api.model("Todo", {
        "title": fields.String(required= True,description="Todo's title"),
        'description': fields.String(required= True,description="Todo's description"),
        'status': fields.String(required= True, default="Pending",description="Todo's status"),
    })

    return todo_model