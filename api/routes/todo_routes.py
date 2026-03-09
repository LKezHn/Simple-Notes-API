from flask_restx import Resource

from api.namespaces.namespaces import todo_ns
from api.models.todo_model import todo_model

todo_model = todo_model(todo_ns)

@todo_ns.route('/')
class Todos(Resource):
    @todo_ns.doc(description="Get all todos",
                 responses={
                    200: 'User logged',
                    400: "Incorrect user or password"
                }
            )
    def get(self):
        pass
    
    @todo_ns.doc(description="Get one todo",
                responses={
                200: 'User logged',
                400: "Incorrect user or password"
            }
        )
    
    @todo_ns.doc(description="Add a new todo",
                 params={
                     "title": "Todo title",
                     "description": "Todo description"
                 },
                 responses={
                    200: 'User logged',
                    400: "Incorrect user or password"
                }
            )
    @todo_ns.expect(todo_model)
    def post(self):
        pass

@todo_ns.route('/<string:todo_id>')
class Todo(Resource):
    @todo_ns.doc(description="Get one todo",
                 responses={
                    200: 'Todo exists',
                    400: "Todo doesn't exists"
                }
            )
    def get(self, todo_id):
        return { "Info": todo_id}

    @todo_ns.doc(description="Update a todo",
                 responses={
                    200: 'Todo updated',
                    400: "Todo doesn't updated or not exists"
                }
            )
    def put(self, todo_id):
        return { "Info": todo_id}
    
    @todo_ns.doc(description="Delete a todo",
                responses={
                200: 'Todo was deleted',
                400: "Todo doesn't was deleted"
            }
        )
    def delete(self, todo_id):
        return { "Info": todo_id}