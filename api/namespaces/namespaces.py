from flask_restx import Namespace

auth_ns = Namespace("auth", description = "User's auth operations")

authorizations = {"Bearer": { "type": "apiKey", "in": "header", "name": "Authorization" }}

todo_ns = Namespace("todo", description = "Todo's operations", authorizations=authorizations)

from api.routes import auth_routes
from api.routes import todo_routes