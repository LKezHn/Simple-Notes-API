from flask_restx import fields

def auth_models(api):

    login_model = api.model("Login", {
        "username": fields.String(required=True, description = "Username"),
        'password': fields.String(required=True, description ="User's password")
    })

    register_model = api.model("Register", {
        "username": fields.String(required=True, description = "Username"),
        "email": fields.String(required=True, description = "User's email"),
        'password': fields.String(required=True, description = "User's password")
    })

    return login_model, register_model