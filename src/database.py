""" Работа с БД """

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PollsConnection:
    """ Подключение и работа с БД """

    def __init__(self, data_database: dict[str, str]) -> None:
        self.user = data_database["user"]
        self.password = data_database["password"]
        self.host = data_database["host"]
        self.port = data_database["port"]
        self.database = data_database["database"]
        self._initialization()

    def _initialization(self) -> None:
        try:
            connection, cursor = self._create_database()
        except:
            print("База данных '{0}' уже существует".format(self.database))
            connection, cursor = self._connect_to_database()

        try:
            self._create_table_polls(connection, cursor)
        except:
            print("Таблица 'polls' уже существует")

        if connection:
            self._close_connection(connection, cursor)
            print("Соединение с PostgreSQL успешно установлено")

    def _create_database(self) -> list[object]:
        connection = psycopg2.connect(user = self.user,
                                    password = self.password,
                                    host = self.host,
                                    port = self.port)

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_create_database = "CREATE DATABASE {0}".format(self.database)
        cursor.execute(sql_create_database)
        print("Создание БД {0}".format(self.database))
        return [connection, cursor]

    def _connect_to_database(self) -> list[object]:
        connection = psycopg2.connect(user = self.user,
                                    password = self.password,
                                    host = self.host,
                                    port = self.port,
                                    database = self.database)
        cursor = connection.cursor()
        return [connection, cursor]

    @staticmethod
    def _create_table_polls(connection: object, cursor: object) -> None:
        create_table_query = '''CREATE TABLE polls
                            (ID       INT              NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            TITLE     VARCHAR(100)     NOT NULL,
                            VARIANTS  TEXT             NOT NULL,
                            ANSWERS   VARCHAR(100)     NOT NULL); '''

        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица 'polls' успешно создана")

    @staticmethod
    def _close_connection(connection: object, cursor: object) -> None:
        cursor.close()
        connection.close()

    def add_new_poll(self, data: dict[str, str]) -> None:
        """ Создание нового голосования """
        connection, cursor = self._connect_to_database()

        insert_query = \
            "INSERT INTO polls (TITLE, VARIANTS, ANSWERS) VALUES ('{0}', '{1}', '{2}')".format(
            data['title'], data['variants'], data['answers']
        )
        cursor.execute(insert_query)
        connection.commit()

        self._close_connection(connection, cursor)