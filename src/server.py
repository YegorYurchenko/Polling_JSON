""" module server.py """
import os
from flask import json
from flask import Flask, redirect
from flask_swagger_ui import get_swaggerui_blueprint

APP = Flask(__name__)

def run_server():
    """ Работа сервера """

    @APP.route('/')
    def index():
        return redirect('/apidocs/')


    @APP.route("/createPoll/", methods=['POST'])
    def createPoll():
        pass

    @APP.route("/poll/", methods=['POST'])
    def poll():
        pass

    @APP.route("/getResult/", methods=["POST"])
    def get_result():
        pass


    @APP.route("/apispec", methods=["GET"])
    def apispec():
        folder = os.path.dirname(os.path.abspath(__file__))
        file = open(os.path.join(folder, "swagger_config.yaml"), 'r', encoding='utf-8')
        return file.read()


    swagger_url = '/apidocs'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        '/apispec',
        config={
            'app_name': "Голосование"
        },
    )

    APP.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)
    APP.run(port=8000)
