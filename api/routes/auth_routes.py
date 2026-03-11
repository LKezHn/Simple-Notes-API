from flask import request
from flask_restx import Resource

from api.namespaces.namespaces import auth_ns
from api.models.user_model import auth_models
from api.controllers.auth_controller import register_user

login_model, register_model = auth_models(auth_ns)

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.doc(description="Login endpoint",
             params={
                 "username": "User name",
                 "password": "User's password"
             },
             responses={
                 200: 'User logged',
                 400: "Incorrect user or password"
             }
        )
    @auth_ns.expect(login_model)
    def post(self):
        return {"status": 200, "token": "JSON Web Token"}
    
@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.doc(description="Register endpoint",
             responses={
                 200: 'User logged',
                 400: "Incorrect user or password"
             }
        )
    @auth_ns.expect(register_model)
    def post(self):
        username = request.json["username"]
        email = request.json["email"]
        password = request.json["password"]

        message, error = register_user(username, email, password)
    
        if error != None:
            return { "status": 400, "message": error}

        return { "status": 200, "message": message}