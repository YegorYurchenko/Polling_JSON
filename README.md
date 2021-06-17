# ![Pooling](project-logo.png)

## Общая информация

Задание - https://github.com/avito-tech/mi-trainee-task-2021

При работе использовался [Python](https://www.python.org/) версии [3.9.5](https://www.python.org/downloads/release/python-395/) и [Flask](https://flask-doc.readthedocs.io/en/latest/) версии [2.0.1](https://pypi.org/project/Flask/).

Frontend реализован с помощью [Swagger](https://swagger.io/).

## Установка

1. Клонируйте репозиторий: `git clone https://github.com/YegorYurchenko/Polling_JSON.git`
1. Перейдите в папку Polling_JSON и создайте виртуальное окружение (в консоли): `py -m venv env`
1. `Необязательно`: если вы используете VS Code, то установите расширение `Python`, зажмите `Ctrl+Shift+P`, напишите `Python: Select Interpreter` и выберите `Enter interpreter path...` -> `Find...` -> `env/Scripts/python.exe`
1. Запустите виртуальное окружение: `env/Scripts/activate`
1. Установите зависимости: `pip install -r requirements.txt`
1. Перейдите в папку `src`: `cd src`

## Подключение базы данных PostgreSQL

1. Если у вас не установлена БД PostgreSQL, то скачайте её по [ссылке](https://www.postgresql.org/download/) и начните установку (в данном проекте использовалась версия 13.3)
1. `Важно`: во время установки запомните `password` и `port`, которые вы введёте, т.к. это понадобится для запуска проекта. Если вы установите `password: 12345` и `port: 5432`, то следующий пункт пропустите
1. После установки зайдите в файл `Polling_JFON/src/server.py` и вставьте значения `password` и `port` словаря `data_database`, которые вы указали при установке PostgreSQL

## Запуск

`py main.py` - запуск проекта. После запуска сборки заработает локальный сервер по адресу `http://127.0.0.1:8000/`

## Структура проекта

* `env` - виртуальное окружение
* `src` - исходники
    * `database.py` - подключение к БД PostgreSQL и взаимодействие с ней
    * `main.py` - файл запуска проекта
    * `server.py` - обработка запросов
    * `swagger_config.yaml` - конфигурация Swagger
    * `utils.py` - вспомогательные функции
* `.gitignore`
* `README.md`
* `requirements.txt` - необходимые зависимости
