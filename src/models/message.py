from flask_restx import fields

facts_model = {
    'name': fields.String('Fact name'),
    'value': fields.String('Fact title')
}

message_model_definition = {
    'message':
    fields.String('Body of the message to send', required=True),
    'from':
    fields.String('User that sends the message', required=True)
}

message_card_model = {
    'title': fields.String('Card title'),
    'activity_title': fields.String('Activity title'),
    'activity_subtitle': fields.String('Activity subtitle'),
    'activity_image': fields.String('Activity image url'),
    'activity_text': fields.String('Activity text'),
    'facts': fields.List(fields.Nested(facts_model)),
    'section_text':
    fields.String('Section image description text'),
    'section_image': fields.String('Section image url'),
    'section_image_title': fields.String('Section image url')
}
