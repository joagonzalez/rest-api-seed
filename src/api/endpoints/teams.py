from flask_restx import Namespace, Api, Resource, fields
from services.LoggerService import loggerService
from services.MSTeamsService import send_teams_message, send_teams_card_message, send_teams_test_message
from models.message import message_model_definition, message_card_model, facts_model

loggerService.info("initializing namespace with Teams endpoints from " + str(__name__))

api = Namespace('MicrosoftTeams', description='Endpoints for Microsoft Teams integration')

# models
message_model = api.model('Message model', message_model_definition)
facts_model = api.model('Facts card message model', facts_model)
message_card_model = api.model('Card message model', {
    'title': fields.String('Card title'),
    'activity_title': fields.String('Activity title'),
    'activity_subtitle': fields.String('Activity subtitle'),
    'activity_image': fields.String('Activity image url'),
    'activity_text': fields.String('Activity text'),
    'facts': fields.List(fields.Nested(facts_model)),
    'section_text': fields.String('Section image description text'),
    'section_image': fields.String('Section image url'),
    'section_image_title': fields.String('Section image url')
})


@api.route('/sendTextMessage')
class SendTextMessage(Resource):
    @api.expect(message_model, validate=True)
    def post(self):
        loggerService.info("Sending a message to MS Teams")
        message = api.payload
        send_teams_message(message['from'] + ': ' + message['message'])
        return {
            'channel': 'DevOps',
            'organization': 'Newtech',
            'message': message['message'],
            'from': message['from']
        }


@api.route('/sendCardMessage')
class SendCardMessage(Resource):
    @api.expect(message_card_model)
    def post(self):
        loggerService.info("Sending a message to MS Teams")
        message = api.payload
        return send_teams_card_message(message['title'], message['activity_title'], message['activity_subtitle'],
                                       message['activity_image'], message['activity_text'],
                                       message['facts'], message['section_text'],
                                       message['section_image'], message['section_image_title'])


@api.route('/sendTestMessage')
class SendTestMessage(Resource):
    def get(self):
        loggerService.info("Sending a test template message to MS Teams")
        return send_teams_test_message()
