from flask import request
from flask_restx import Resource

from flask_jwt_extended import jwt_required, get_jwt_identity

from api.namespaces.namespaces import todo_ns
from api.models.todo_model import todo_model

from api.controllers.todo_controller import get_todos, add_todo, get_todo, update_todo, delete_todo

todo_model = todo_model(todo_ns)

@todo_ns.route('/')
@todo_ns.doc(security="Bearer")
class Todos(Resource):
    @todo_ns.doc(description="Get all todos", responses={ 200: 'User logged', 400: "Incorrect user or password"})
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        todos = get_todos(user_id)

        return {"status": 200, "todos": todos}

    @todo_ns.doc(description="Add a new todo", responses={ 200: 'User logged', 400: "An error was ocurred"})
    @todo_ns.expect(todo_model)
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        title, description, status = request.json.values()
        todo = add_todo(title, description, status, user_id)

        return { "status": 200, "todo": todo }

@todo_ns.route('/<string:todo_id>')
@todo_ns.doc(security="Bearer")
class Todo(Resource):
    @todo_ns.doc(description="Get one todo", responses={ 200: 'Todo exists', 400: "Todo doesn't exists" })
    @jwt_required()
    def get(self, todo_id):
        user_id = get_jwt_identity()

        todo, error = get_todo(todo_id, user_id)
        if error != None:
            return { "status": 400, "message": error }
        
        return { "status": 200, "todo": todo}

    @todo_ns.doc(description="Update a todo", responses={ 200: 'Todo updated', 400: "Todo doesn't updated or not exists" })
    @todo_ns.expect(todo_model)
    @jwt_required()
    def put(self, todo_id):
        user_id = get_jwt_identity()

        title, description, status = request.json.values()

        todo, error = update_todo(todo_id, user_id, title, description, status)
        
        if error != None:
            return { "status": 400, "message": error }
        
        return { "status": 200, "message": "todo updated","todo": todo}
    
    @todo_ns.doc(description="Delete a todo", responses={ 200: 'Todo was deleted', 400: "Todo doesn't was deleted" })
    @jwt_required()
    def delete(self, todo_id):
        user_id = get_jwt_identity()

        message, error = delete_todo(todo_id, user_id)
        if error != None:
            return { "status": 400, "message": error }
        
        return { "status": 200, "message": message}