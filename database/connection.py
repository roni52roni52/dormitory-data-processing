import mysql.connector


class DatabaseConnection:
    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        database: str,
    ):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )

    def get_connection(self):
        return self.connection

    def close(self):
        if self.connection.is_connected():
            self.connection.close()