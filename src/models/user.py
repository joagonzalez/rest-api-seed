from flask_restx import fields

message_model = {
    'name': fields.String('Username'),
    'password': fields.String('User password'),
    'email': fields.String('User email'),
    'creation': fields.String('User creation date'),
    'enable': fields.String('User enable status'),
}
