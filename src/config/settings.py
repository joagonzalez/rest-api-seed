config = {
    'FLASK' : {
        'DEBUG': True,
        'HOSTNAME': '127.0.0.1',
        'PORT': 5000,
        'LOGGER': 'app_debug'
    },
    'RESTX': {
        'VERSION': {'APP1': '1.0.0', 'APP2': '2.0.1'},
        'TITLE': 'REST API',
        'RESTPLUS_SWAGGER_UI_DOC_EXPANSION': 'list',
        'DESCRIPTION': 'App that expose different functionalities through REST API using Flask and Flask-restx.',
        'RESTPLUS_VALIDATE': True,
        'RESTPLUS_MASK_SWAGGER': False,
        'RESTPLUS_ERROR_404_HELP': False
    },
    'TEAMS': {
        'WEBHOOK_URL': 'https://outlook.office.com/webhook/327044bc-8860-4705-a521-48cc9bfd264e@58005ddb-3d82-4718-9e75-ec5c71cca7ec/IncomingWebhook/ce255d45adfd4d94aa803a84e86e1d6f/4b94f775-45ba-4f8d-a767-252cb12f9726'
    }
}
