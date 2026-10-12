import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from types import TracebackType


class DatabaseConnection:
    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        database: str,
    ) -> None:
        self.connection: MySQLConnectionAbstract = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )

    def get_connection(self) -> MySQLConnectionAbstract:
        return self.connection

    def __enter__(self) -> MySQLConnectionAbstract:
        return self.connection

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()

    def close(self) -> None:
        if self.connection.is_connected():
            self.connection.close()