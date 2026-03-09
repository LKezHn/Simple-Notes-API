from flask_restx import Namespace

auth_ns = Namespace("auth", description = "User's auth operations")

todo_ns = Namespace("todo", description = "Todo's operations")

from api.routes import auth_routes
from api.routes import todo_routes