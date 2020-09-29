from config.settings import config
from flask import Blueprint
from flask_restx import Api
from services.LoggerService import loggerService
from api.endpoints.teams import api as ns_teams
from api.endpoints.users import api as ns_users
from models.message import message_model_definition, message_card_model, facts_model

loggerService.info("initializing blueprint api v2")

blueprint = Blueprint("api app 2", __name__, url_prefix='/app2/api')

api = Api(blueprint, title='API APP 2', version=config['RESTX']['VERSION']['APP2'])
api.add_namespace(ns_teams)
api.add_namespace(ns_users)
