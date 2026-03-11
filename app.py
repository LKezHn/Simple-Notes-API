from flask import Flask, request 
from flask_restx import Api

from config import Config
from db import mongo, create_indexes

from api.namespaces.namespaces import auth_ns, todo_ns

app = Flask(__name__)
app.config.from_object(Config)

mongo.init_app(app)

with app.app_context():
    create_indexes()

api = Api(app, 
          version='1.0', 
          title="Simple Notes API", 
          description="An example of a simple API with CRUD methods and auth"
        )

api.add_namespace(auth_ns)
api.add_namespace(todo_ns)

if __name__ == "__main__":
    app.run(debug=True)