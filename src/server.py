""" module server.py """
import os
from flask import Flask, jsonify, request, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from database import PollsConnection
from utils import delete_empty_variants, get_initial_answers

APP = Flask(__name__)

data_database = {
    "user": "postgres",
    "password": "12345",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "polls_postgres_db"
}

POLLS = PollsConnection(data_database)


def run_server():
    """ Работа сервера """

    @APP.route('/')
    def index():
        return redirect('/apidocs/')


    @APP.route("/createPoll/", methods=['POST'])
    def create_poll():
        try:
            data = request.get_json()
            data['variants'] = delete_empty_variants(data['variants'])
            data['answers'] = get_initial_answers(data['variants'])
        except Exception:
            return 'Некорректный json-объект', 400

        try:
            message = "Голосование '{}' успешно создано".format(data['title'])
            POLLS.add_new_poll(data)
            return jsonify({'result': 'success', 'message': message})
        except Exception:
            return 'Непредвиденная ситуация', 500

    @APP.route("/poll/", methods=['POST'])
    def poll():
        try:
            data = request.get_json()
        except Exception:
            return 'Некорректный json-объект', 400

        if data['poll_id'] < 1 or data['choice_id'] < 1:
            return 'Нет такого голосования или варианта ответа', 500

        try:
            message = "Вы успешно проголосовали за вариант '{}'".format(data['choice_id'])
            POLLS.vote(data['poll_id'], data['choice_id'])
            return jsonify({'result': 'success', 'message': message})
        except Exception:
            return 'Не получилось проголосовать. Нет такого голосования или варианта ответа', 500

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
