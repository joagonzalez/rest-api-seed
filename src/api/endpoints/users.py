from flask_restx import Namespace, Api, Resource
from services.LoggerService import loggerService

loggerService.info("initializing namespace with Teams endpoints from "
                   + str(__name__))

api = Namespace('UserManagement', description='Endpoints for user management')


# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        loggerService.info("alguien entro a hello!")
        return {'hello': 'world'}
