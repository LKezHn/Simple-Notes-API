from flask_restx import Resource

from api.namespaces.namespaces import auth_ns
from api.models.user_model import auth_models

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
        pass
    
@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.doc(description="Register endpoint",
             params={
                 "username": "User name",
                 "email": "User's email",
                 "password": "User's password"
             },
             responses={
                 200: 'User logged',
                 400: "Incorrect user or password"
             }
        )
    @auth_ns.expect(register_model)
    def post(self):
        pass
    
