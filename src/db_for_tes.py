class DataBaseConnector:
    def __init__(self) -> None:
        pass

    def connect(self):
        print("Соединение установлено")

        class Connection:
            def __init__(self) -> None:
                pass

            def close(self):
                print("Соединение закрыто")
                return "Соединение закрыто"

        return Connection()


db_connector = DataBaseConnector()
# connection = db_connector.connect()
# connection.close()
