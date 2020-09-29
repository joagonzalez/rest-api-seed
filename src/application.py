from flask import Flask
from config.settings import config
from api.app1.api import blueprint as bp_app1
from api.app2.api import blueprint as bp_app2


class Application:

    def __init__(self):
        self.app = Flask(__name__)
        self.create()

    def __str__(self):
        pass

    def message(self):
        """
        Startup message
        """
        print("""
  _____  ______  _____ _______            _____ _____
 |  __ \|  ____|/ ____|__   __|     /\   |  __ \_   _|
 | |__) | |__  | (___    | |______ /  \  | |__) || |
 |  _  /|  __|  \___ \   | |______/ /\ \ |  ___/ | |
 | | \ \| |____ ____) |  | |     / ____ \| |    _| |_
 |_|  \_\______|_____/   |_|    /_/    \_\_|   |_____|
        """)

    def config(self):
        """
        Configure all the parameters required by Flask App
        """
        self.app.config['SWAGGER_UI_DOC_EXPANSION'] = config['RESTX']['RESTPLUS_SWAGGER_UI_DOC_EXPANSION']
        self.app.config['RESTPLUS_VALIDATE'] = config['RESTX']['RESTPLUS_VALIDATE']
        self.app.config['RESTPLUS_MASK_SWAGGER'] = config['RESTX']['RESTPLUS_MASK_SWAGGER']
        self.app.config['ERROR_404_HELP'] = config['RESTX']['RESTPLUS_ERROR_404_HELP']

    def create(self):
        """
        Flask app bootstrap
        """
        self.config()
        self.app.register_blueprint(bp_app1)
        self.app.register_blueprint(bp_app2)

    def run(self):
        self.message()
        self.app.run(host=config['FLASK']['HOSTNAME'], port=config['FLASK']['PORT'], debug=config['FLASK']['DEBUG'])
